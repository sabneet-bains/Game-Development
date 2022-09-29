import grpc
import logging
import queue
import random
from concurrent import futures
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generated_sources import Network_pb2_grpc
from generated_sources import Network_pb2 as nw

from models import Account
from models import Game
from models import Player
from models import Card
from models import GameStatus


# GRPC server implementation
class NetworkGrpcService(Network_pb2_grpc.NetworkServiceServicer):

    # Holds a message queue for each connected user to distribute updates
    streams = {}
    # An empty marker update that can be inserted into a queue to terminate the stream
    terminate_flag = nw.GameUpdate()

    def __init__(self):
        engine = create_engine("mysql://clueless:Password1@localhost/clueless")
        self.session = sessionmaker(bind=engine)()

    # Create a new hosted game
    def createGame(self, request, context):

        print("Create game request received")
        account = self.__get_account(request.name)

        suspect_id = random.randrange(start=1, stop=6, step=1)
        room_id = random.randrange(start=7, stop=15, step=1)
        weapon_id = random.randrange(start=16, stop=21, step=1)
        ###
        # Code to create game and player entries goes here
        game = Game(
            status='created',
            suspect_id=suspect_id,
            room_id=room_id,
            weapon_id=weapon_id
        )
        self.session.add(game)
        self.session.commit()

        print(f'Created new Game entry:\nid = {game.id}\nstatus = {game.status}\nweapon = {game.weapon_id}\nsuspect = {game.suspect_id}\n room = {game.room_id}\n\n')

        player = Player(
            account_id=account.id,
            game_id=game.id,
            number=1,
            name=request.name
        )
        self.session.add(player)
        ###

        self.session.commit()
        return self.__stream_updates(player)

    # Connect user to pending or in-progress game and subscribe to all game updates
    def connectToGame(self, request, context):

        print("Connect to game request received")
        account = self.__get_account(request.name)

        ###
        # Code to players in the existing game they are trying to join
        players = self.session.query(Player).filter_by(game_id=request.gameID).all()
        if len(players) < 6:
            # create new player
            player = Player(
                account_id=account.id,
                game_id=request.gameID,
                number=1,
                name=request.name
            )
            # add player to session
            self.session.add(player)
        else:
            print("The game is already filled!")
        ###

        self.session.commit()
        return self.__stream_updates(player)

    # Move a pending game to in-progress once enough players are connected
    def startGame(self, request, context):
        print("Received start game request")

        ###
        # Switch game status to started, fetch all players, and send them the initiate message
        players = self.session.query(Player).filter_by(game_id=request.gameID).all()
        game = self.session.query(Game).filter_by(id=request.gameID).first()
        game.status = 'started'

        # Create a list of all valid card IDs and deal them out
        card_ids = [*range(1, 22, 1)]
        card_ids.remove(game.weapon_id)
        card_ids.remove(game.room_id)
        card_ids.remove(game.suspect_id)

        i = 0
        while len(card_ids) > 0:
            random_card = random.choice(card_ids)
            card_ids.remove(random_card)
            card = self.session.query(Card).filter_by(id=random_card).first()
            players[i % len(players)].cards.append(card)
            i += 1

        character_ids = [*range(1, len(players) + 1, 1)]
        pcs = []

        self.session.commit()

        for player in players:
            character = random.choice(character_ids)
            player.number = character
            character_ids.remove(character)
            pcs.append(nw.PlayerCharacter(playerID=player.id, character=character, name=player.name))

        # Persist player numbers to the database
        self.session.commit()

        for player in players:
            cards = []
            for card in player.cards:
                cards.append(card.id)

            if player.id in NetworkGrpcService.streams.keys():
                initiate = nw.InitiateGame()
                initiate.cards.extend(cards)
                initiate.characters.extend(pcs)
                update = nw.GameUpdate(
                    gameID=request.gameID,
                    playerID=player.id,
                    number=1,
                    type=nw.GameUpdate.INITIATE,
                    initiate=initiate
                )

                NetworkGrpcService.streams[player.id].put(update)

        return nw.Acknowledgement(success=True, message="Received request: " + str(request))

        # Validate, record, and react to the actions of a player turn

    def submitMove(self, request, context):
        print("Received submit move request: " + str(request))

        player = self.session.query(Player).filter_by(id=request.playerID).first()
        game = self.session.query(Game).filter_by(id=player.game_id).first()

        # If the suspect field is empty then this is just a location update, send it out
        if not request.suspect:
            self.__turn_summary(game, player, None, request.location, -1, -1)
            return nw.Acknowledgement(success=True, message="Received turn with just move and no suggestion")

        # Get all players that have at least one of the suggested cards (minus the current player)
        players = self.session.query(Player)\
            .filter(Player.id != player.id, Player.game == game, Player.cards.any(Card.id.in_([request.location, request.suspect, request.weapon]))).all()

        # If no one had the cards, just notify everyone of the turn and start a new turn
        if not players or len(players) == 0:
            self.__turn_summary(game, player, request.suspect, request.location, request.weapon, -1)
            return nw.Acknowledgement(success=True, message="No players had suggested cards, initiating next turn")

        print('Finding player to disprove')
        # Find the player who needs to disprove (earliest in upcoming turn order)
        disproving_player = None
        for p in players:
            print(f'Player: {p.id} - {p.name}')
            if not disproving_player:
                disproving_player = p
            elif ((p.number > player.number) or ((p.number < player.number) and (disproving_player.number < player.number))) and (p.number < disproving_player.number):
                disproving_player = p
        print(f'Disproving player is {disproving_player.id}')

        # Prompt this player to disprove a card
        if disproving_player.id in NetworkGrpcService.streams.keys():
            prompt = nw.PromptToDisprove()
            prompt.cards.extend([request.weapon, request.suspect, request.location])
            NetworkGrpcService.streams[disproving_player.id].put(
                nw.GameUpdate(gameID=game.id,
                              playerID=player.id,
                              number=1,
                              type=nw.GameUpdate.PROMPT,
                              prompt=prompt))

        # Send the turn summary out to everyone
        self.__turn_summary(game, player, request.suspect, request.location, request.weapon, disproving_player.id)

        return nw.Acknowledgement(success=True, message="Received request: " + str(request))

    # Process a player's request to disprove one of the suggestions
    def disprove(self, request, context):
        print("Received disprove request: " + str(request))

        # Get the player who should be forwarded the disproven card info
        player = self.session.query(Player).filter_by(id=request.playerID).first()

        if player.id in NetworkGrpcService.streams.keys():
            NetworkGrpcService.streams[player.id].put(nw.GameUpdate(
                gameID=request.gameID,
                playerID=player.id,
                number=request.disprovingCharacter,
                type=nw.GameUpdate.DISPROVE,
                disprove=request.card))

        return nw.Acknowledgement(success=True, message="Received request: " + str(request))

    # Submit an accusation
    def accuse(self, request, context):
        print("Received accusation: " + str(request))

        player = self.session.query(Player).filter_by(id=request.playerId).first()
        correct = (request.accusing.location == player.game.room_id and request.accusing.suspect == player.game.suspect_id and request.accusing.weapon == player.game.weapon_id)
        print(f'Accusation was... {correct}')
        self.__next_turn(player)
        return nw.AccusationResponse(correct=correct)

    # Return the full history for a game so far if the player is allowed to see it
    def requestHistory(self, request, context):
        print("Received game history request: " + str(request))
        game_history = nw.GameHistory()
        sample_update = nw.GameUpdate(gameID=1, playerID=1, number=1, type=nw.GameUpdate.Type.INITIATE)
        game_history.updates.extend([sample_update])
        return nw.GameHistory()

    # Remove this player from the streams and cleanly disconnect the client
    def disconnect(self, request, context):
        NetworkGrpcService.streams[request.playerId].put(NetworkGrpcService.terminate_flag)

        return nw.Acknowledgement(success=True, message='Terminating stream')

    def __next_turn(self, current_player):
        print(f'Current player taking turn: {current_player.id} - {current_player.number} - {current_player.name}')
        players = self.session.query(Player).filter_by(game=current_player.game).all()
        next_number = current_player.number + 1
        if next_number > len(players):
            next_number = 1
        next_player = self.session.query(Player).filter_by(game=current_player.game, number=next_number).first()
        print(f'Next player taking turn: {next_player.id} - {next_player.number} - {next_player.name}')
        print(f'Starting turn for player number {next_player.number}')
        for player in players:
            NetworkGrpcService.streams[player.id].put(nw.GameUpdate(
                gameID=player.game.id,
                playerID=next_player.id,
                type=nw.GameUpdate.Type.NEXTTURN
            ))

    def __turn_summary(self, game, current_player, suspect, room, weapon, disprover_id):
        players = self.session.query(Player).filter_by(game=game)
        # Include the disproven card for the player whose turn it was
        for player in players:
            NetworkGrpcService.streams[player.id].put(nw.GameUpdate(
                gameID=game.id,
                playerID=current_player.id,
                type=nw.GameUpdate.Type.TURN,
                turn=nw.PlayerTurn(
                    playerID=current_player.id,
                    room=room,
                    suspect=suspect,
                    weapon=weapon,
                    disprovingPlayer=disprover_id,
                    location=room
                )
            ))

    def __get_account(self, name):
        account = self.session.query(Account).filter_by(name=name).first()
        if account:
            return account
        else:
            account = Account(name=name)
            self.session.add(account)
            self.session.commit()
            return account

    # This registers a new queue to send messages to this player into the streams dictionary, and then sets
    # up a loop to forward game updates on to that player when they appear in the queue
    def __stream_updates(self, player):
        yield nw.GameUpdate(playerID=player.id, gameID=player.game_id, type=nw.GameUpdate.CONNECT)
        # Create a queue that will be passed any updates to forward to the client
        update_queue = queue.Queue()
        # Add queue to dictionary of active connections, keyed by game and player ID
        NetworkGrpcService.streams[player.id] = update_queue
        try:
            while True:
                # Wait for an update to appear on the queue
                update = update_queue.get()
                # If the received update is the terminate flag, break out and terminate the stream
                if update == NetworkGrpcService.terminate_flag:
                    print(f'Terminated stream for player {player.id}')
                    del NetworkGrpcService.streams[player.id]
                    break
                print(f'Sending a new update out to stream for player {player.id}')
                yield update
        except:
            del NetworkGrpcService.streams[player.id]
            print("Exception, dropped out")


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=[('grpc.keepalive_time_ms', 1000)])
    Network_pb2_grpc.add_NetworkServiceServicer_to_server(NetworkGrpcService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
