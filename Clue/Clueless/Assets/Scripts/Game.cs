using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * This script creates an inherited class called “Game” based on the base unity “MonoBehaviour” class
 * along with new methods for Setting a hand, starting a turn, starting a disproval, updating positions,
 * handling updates, getting cards by id, getting a card, win, and lose!
 */

public class Game : MonoBehaviour
{
    public UIManager uiManager;
    // These have all been passed in using the Unity UI, they don't need to be constructed
    public List<Card> deck;
    public List<PlayerTurn> moves;
    public List<Location> hallways;

    public int gameID;
    public int playerID;

    public Player player;
    public bool gameOver = false;

    public CameraController cameraController;

    // Map from character ID to controlling player
    public Dictionary<int, Character> pcs = new Dictionary<int, Character>();

    private Character current;

    // Populate the player's hand with cards based on their ID, and mark them disproven
    public IEnumerator SetHand(IEnumerable<int> cards)
    {
        player.AddToHand(GetCardsById(cards));
        foreach (int card_id in cards)
        {
            Card card = GetCard(card_id);
            player.AddToHand(card);

            // Add the card model to the player's visible hand
            card.cardObject.GetComponent<CardController>().AddToHand();
            card.Disprove();
            yield return new WaitForSeconds(0.2f);
        }
        // uiManager.ShowHand(player);
    }

    // Initiate the action and options when it becomes this player's turn
    public void StartTurn(Character character)
    {
        if (character == this.player.character)
        {
            Debug.Log("Starting my turn");
            // Enable controls to move to an adjacent space
            uiManager.MoveOptions(player);

        } else
        {
            // Show that we are waiting for another player
            uiManager.WaitingForTurn(character);
            Debug.Log("Starting " + character.name + "'s turn");
        }
    }

    public void StartDisprove(List<Card> cards, int suggestingPlayer)
    {
        // Enable the disprove UI with the correct cards
        uiManager.Disprove(cards, this.player, suggestingPlayer);
    }

    // Move all characters and weapons to a location based on a player turn game update
    public void UpdatePositions(GameUpdate update)
    {
        // Move the player to their new location
        Character character = pcs[update.PlayerID];
        Location location = (Location)GetCard(update.Turn.Location);
        if (location == null)
        {
            location = hallways.Find(i => i.id == update.Turn.Location);
        }
        character.Move(location);
        // If they made a suggestion, move the supsect to the new location
        if (update.Turn.Suspect > 0 && update.Turn.Location > 0)
        {
            Character suspect = (Character)GetCard(update.Turn.Suspect);
            suspect.Move(location);
            Weapon weapon = (Weapon)GetCard(update.Turn.Weapon);
            weapon.Move(location);
        }
    }

    // Triggered when a suggestion was made but no one had cards to disprove
    public void NoDisprove(List<Card> suggestedCards)
    {
        // Check all the suggested cards. For any that aren't in our hand,
        // disprove ALL others of this type
        foreach (Card card in suggestedCards)
        {
            // This is a mess of a way to do this but whatever it was fast and it works
            if (!player.CardInHand(card) && (1 <= card.id) && (card.id <= 6))
            {
                for (int i = 1; i < 7; i++)
                {
                    if (i != card.id)
                    {
                        GetCard(i).Disprove();
                    }
                }
            }
            else if (!player.CardInHand(card) && (7 <= card.id) && (card.id <= 15))
            {
                for (int i = 7; i < 16; i++)
                {
                    if (i != card.id)
                    {
                        GetCard(i).Disprove();
                    }
                }
            }
            else if (!player.CardInHand(card) && (16 <= card.id) && (card.id <= 21))
            {
                for (int i = 16; i < 22; i++)
                {
                    if (i != card.id)
                    {
                        GetCard(i).Disprove();
                    }
                }
            }
        }

        uiManager.AccuseQuestion();
    }

    private void ShowTurn(GameUpdate update)
    {
        Card location = GetCard(update.Turn.Location);
        Card suspect = GetCard(update.Turn.Suspect);
        Card weapon = GetCard(update.Turn.Weapon);

        string disprover = "No one";
        if (update.Turn.DisprovingPlayer >= 0)
        {
            disprover = pcs[update.Turn.DisprovingPlayer].name;
        }
        uiManager.ShowTurn(pcs[update.PlayerID].name, location, suspect, weapon, disprover);

        cameraController.ShowLocation(location);
    }

    public void HandleUpdate(GameUpdate update)
    {
        if (update.Type == GameUpdate.Types.Type.Initiate)
        {
            uiManager.Initiate();
            // Set up the players and characters
            foreach (PlayerCharacter pc in update.Initiate.Characters)
            {
                Player newPlayer =  new Player(pc.PlayerID, pc.Name, (Character)GetCard(pc.Character));
                pcs.Add(pc.PlayerID, (Character)GetCard(pc.Character));
                newPlayer.character.name = pc.Name;

                Debug.Log("My player ID is: " + playerID);
                // Save a special reference to our own player
                if (pc.PlayerID == this.playerID)
                {
                    this.player = newPlayer;
                    StartCoroutine(SetHand(update.Initiate.Cards));
                }
            }

            uiManager.SetName(player);

            // Start the first player's turn
            StartTurn((Character)GetCard(1));

        } else if (update.Type == GameUpdate.Types.Type.Prompt)
        {
            List<Card> cards = GetCardsById(update.Prompt.Cards);
            StartDisprove(cards, update.PlayerID);

        } else if (update.Type == GameUpdate.Types.Type.Turn)
        {
            // If it was our turn and there's no disproving player, skip to accuse
            if (update.Turn.DisprovingPlayer < 1 && update.Turn.PlayerID == this.playerID)
            {
                uiManager.AccuseQuestion();
            }
            // Update locations of characters and weapons
            UpdatePositions(update);

            // Show the results of the turn
            if (update.Turn.Location >= 0)
            {
                ShowTurn(update);
            }

        } else if (update.Type == GameUpdate.Types.Type.Connect)
        {
            // Should receive this as first request on the stream after connecting
            // Use to save the player ID
            this.playerID = update.PlayerID;
            this.gameID = update.GameID;
            uiManager.WaitingForStart(this.gameID);
        } else if (update.Type == GameUpdate.Types.Type.Disprove)
        {
            // Mark the card as disproven
            GetCard(update.Disprove).Disprove();
            // Display what was disproven
            uiManager.ShowCard(GetCard(update.Disprove), (Character)GetCard(update.Number));
            // Ask if the player wants to accuse
            uiManager.AccuseQuestion();
        } else if (update.Type == GameUpdate.Types.Type.Nextturn)
        {
            StartTurn(pcs[update.PlayerID]);
        }
    }

    private List<Card> GetCardsById(IEnumerable<int> ids)
    {
        List<Card> cards = new List<Card>();
        foreach (int i in ids)
        {
            cards.Add(GetCard(i));
        }
        return cards;
    }

    public Card GetCard(int id)
    {
        return deck.Find(c => c.id == id);
    }

    public void Win()
    {
        uiManager.Win();
    }

    public void Lose()
    {
        uiManager.Lose();
    }

}
