using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Grpc.Core;
using TMPro;

/**
 * This script creates an inherited class called “NetworkManager” based on the base unity “MonoBehaviour” 
 * class in order to process server-client communications by creating a game, connecting to a game, 
 * starting a game, submitting a move, making an accusation,  disproving a card, 
 * requesting game log history, disconnecting, acknowledging logs, and handling updates!
 */

public class NetworkManager : MonoBehaviour
{
    public TextMeshProUGUI logText;
    private string host = "clueless.ideologyhole.com:50051";
    // private string host = "localhost:50051";
    private Channel channel;
    private NetworkService.NetworkServiceClient client;

    public TMP_InputField nameInput;
    public TMP_InputField gameIdInput;
    public Game game;

    public List<Card> lastSuggested;

    private void Start()
    {
        List<ChannelOption> options = new List<ChannelOption>();
        options.Add(new ChannelOption("grpc.keepalive_time_ms", 1000));
        channel = new Channel(host, ChannelCredentials.Insecure, options);
        client = new NetworkService.NetworkServiceClient(channel);
    }

    // Send request to create a game and subscribe to updates for that game
    public void CreateGame()
    {
        Debug.Log("Sending create game request with username: " + nameInput.text);
        HandleUpdates(client.createGame(new CreateGameRequest 
        { 
            PlayerID = 1, 
            Name = nameInput.text 
        }));
    }

    public void ConnectToGame()
    {
        Debug.Log("Sending connect to game request with username: " + nameInput.text 
            + " and gameID: " + gameIdInput.text);
        HandleUpdates(client.connectToGame(new ConnectRequest
        {
            GameID = int.Parse(gameIdInput.text),
            PlayerID = 1,
            Name = nameInput.text
        }));
    }

    public void StartGame()
    {
        Debug.Log("Sending start game request");
        Acknowledgement response = client.startGame(new StartGameRequest 
        { 
            PlayerID = game.playerID, 
            GameID = game.gameID 
        });
        LogAcknowledgement(response);
    }

    public void SubmitMove(Location location, Card suspect, Card weapon, Card room)
    {
        if (location.id < 0)
        {
            // If the location is a hall, just send the location ID and no suggestions
            Acknowledgement response = client.submitMove(new Move 
            { 
                PlayerID = game.player.id, 
                Location = location.id
            });
        } else
        {
            // Save the cards we suggested
            lastSuggested = new List<Card>();
            lastSuggested.Add(location);
            lastSuggested.Add(suspect);
            lastSuggested.Add(weapon);

            Debug.Log("Submitting move");
            Acknowledgement response = client.submitMove(new Move 
            { 
                PlayerID = game.player.id, 
                Location = location.id, 
                Suspect = suspect.id, 
                Weapon = weapon.id
            });
            LogAcknowledgement(response);
            // Check if there were no cards to disprove
            if (response.Message.Equals("No players had suggested cards, initiating next turn"))
            {
                game.NoDisprove(lastSuggested);
            }
        }
    }

    public void Accuse(bool isAccusing, Card suspect, Card weapon, Card room)
    {
        if (isAccusing)
        {
            Accusation accusation = new Accusation {
                IsAccusing = true,
                PlayerId = game.player.id,
                Accusing = new Move
                {
                    PlayerID = game.playerID,
                    Suspect = suspect.id,
                    Weapon = weapon.id,
                    Location = room.id
                }
            };
            AccusationResponse response = client.accuse(accusation);
            if (response.Correct)
            {
                game.Win();
            } else
            {
                game.Lose();
            }
        } else
        {
            Accusation accusation = new Accusation
            {
                IsAccusing = false,
                PlayerId = game.player.id,
            };
            client.accuse(accusation);
            Debug.Log("We got to the end");
        }
    }

    public void Disprove(Card card, int player)
    {
        Debug.Log("Disproving card: " + card.id);
        Acknowledgement response = client.disprove(new DisproveRequest { 
            PlayerID = player, 
            GameID = game.gameID, 
            Card = card.id,
            DisprovingCharacter = game.player.character.id
        });
        LogAcknowledgement(response);
    }

    public void RequestHistory()
    {
        Debug.Log("Requesting full game history");
        GameHistory response = client.requestHistory(new HistoryRequest { PlayerID = 1, GameID = 1 });
    }

    public void Disconnect()
    {
        Debug.Log("Disconnecting from server stream");
        Acknowledgement response = client.disconnect(new DisconnectRequest { PlayerId = game.playerID });
        LogAcknowledgement(response);
    }

    private void LogAcknowledgement(Acknowledgement response)
    {
        Debug.Log("Received request Acknowledgement: " + response);
    }

    // Example of an ongoing stream of replies from the demo heartbeat method
    async void HandleUpdates(AsyncServerStreamingCall<GameUpdate> updates)
    {
        IAsyncStreamReader<GameUpdate> stream = updates.ResponseStream;
        while (await stream.MoveNext())
        {
            Debug.Log("Received GameUpdate: " + stream.Current.ToString());
            game.HandleUpdate(stream.Current);
        }
    }

    private void OnDisable()
    {
        Disconnect();
        channel.ShutdownAsync().Wait();
    }
}
        
