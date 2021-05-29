using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

/**
 * This script creates an inherited class called “Card” based on the base unity “MonoBehaviour” class
 * along with new methods for start, waiting prior to start, initiation, showing cards in hand, 
 * waiting for a turn, move options based on location, making a suggestion, making an accusation, 
 * disproving a suggestion, showing a card, setting player name, displaying win, displaying lose, 
 * and GameOver!
 */

public class UIManager : MonoBehaviour
{
    // Global UI, always visible
    public TextMeshProUGUI nameLabel;
    public TextMeshProUGUI handText;
    public TextMeshProUGUI shownCardText;

    // Call back to NetworkManager to send requests from buttons
    public NetworkManager nm;

    // UI on startup
    public GameObject startupUI;

    // UI when waiting for a game to begin
    public GameObject waitingUI;
    public TextMeshProUGUI gameIDText;

    // UI when waiting for another player to take a turn
    public GameObject waitForTurnUI;
    public TextMeshProUGUI currentTurnText;

    // UI when prompted to disprove a suggestion
    public GameObject disproveUI;
    public List<Button> disproveButtons;

    // UI for selecting a location to move to
    public GameObject moveUI;
    public List<Button> moveButtons;

    // UI for selecting suggestions
    public GameObject suggestUI;
    public ToggleGroup suspectToggle;
    public ToggleGroup weaponToggle;
    public ToggleGroup roomToggle;
    public Button submitButton;

    // UI to accuse or not
    public GameObject accusePromptUI;
    public Button yesAccuseButton;
    public Button noAccuseButton;

    // UI displayed on successful accusation
    public GameObject winUI;

    // UI displayed on failed accusation
    public GameObject loseUI;

    // UI displayed after someone has won
    public GameObject gameOverUI;

    // Animator to handle any UI animations
    public Animator animator;

    // Start is called before the first frame update
    void Start()
    {
        startupUI.SetActive(true);
        noAccuseButton.onClick.AddListener(() => {
            nm.Accuse(false, null, null, null);
            accusePromptUI.SetActive(false);
            });
    }

    public void WaitingForStart(int gameId)
    {
        startupUI.SetActive(false);
        waitingUI.SetActive(true);
        gameIDText.SetText("Game ID: " + gameId);
    }

    public void Initiate()
    {
        waitingUI.SetActive(false);
        animator.SetTrigger("Shrink");
    }

    public void ShowHand(Player player)
    {
        handText.gameObject.SetActive(true);
        foreach (Card card in player.hand)
        {
            handText.text += "\n" + card.cardName;
        }
    }

    public void ShowTurn(string player, Card location, Card suspect, Card weapon, string disprover)
    {
        shownCardText.SetText(player + " suggested:\n" + suspect.cardName + 
            "\nin the " + location.cardName + "\nwith the " + weapon.cardName +
            "\n\n" + disprover + " showed a card");
    }

    public void WaitingForTurn(Character character)
    {
        waitForTurnUI.SetActive(true);
        currentTurnText.SetText("Waiting for: " + character.name);
        currentTurnText.color = GameObject.Find(character.name)
            .GetComponent<MeshRenderer>().material.color;
    }

    public void MoveOptions(Player player)
    {
        waitForTurnUI.SetActive(false);
        moveUI.SetActive(true);

        int buttonIndex = 0;
        foreach (Location location in player.character.location.adjacent)
        {
            Button button = moveButtons[buttonIndex];
            button.gameObject.SetActive(true);
            button.GetComponentInChildren<Text>().text = location.cardName;
            button.onClick.RemoveAllListeners();
            // On click, move to this location and save it as my turn move
            button.onClick.AddListener(() => {
                player.character.Move(location);
                player.lastTurnLocation = location;
                this.Suggest(location, false);
            });
            button.interactable = true;

            // If the location is a hallway and it is blocked, disable the button
            if (location.IsBlocked())
            {
                button.interactable = false;
            }
            buttonIndex++;
        }

        // If the current location is a room, make the last button this room
        if (player.character.location.id > 0)
        {
            Button button = moveButtons[buttonIndex];
            button.gameObject.SetActive(true);
            button.GetComponentInChildren<Text>().text = player.character.location.cardName;
            button.onClick.RemoveAllListeners();
            button.onClick.AddListener(() =>
            {
                this.Suggest(player.character.location, false);
            });
            button.interactable = true;

            // If they ended the last turn in this location, disable the button
            if (player.lastTurnLocation == player.character.location)
            {
                button.interactable = false;
            }
            buttonIndex++;
        }

        // If there aren't 5 locations, hide all remaining buttons
        if (buttonIndex < 4)
        {
            for (int i = buttonIndex; i < 5; i++)
            {
                moveButtons[i].gameObject.SetActive(false);
            }
        }

    }

    public void Suggest(Location location, bool accuse)
    {
        // Disable the movement UI
        moveUI.SetActive(false);

        // If the location is a hallway, end our turn now
        if (location.id < 0 && !accuse)
        {
            nm.SubmitMove(location, null, null, null);
            return;
        }

        // Display the toggles to select cards to suggest
        suggestUI.SetActive(true);
        Game game = GameObject.Find("GameManager").GetComponent<Game>();
        List<Toggle> toggles = new List<Toggle>();
        toggles.AddRange(suspectToggle.GetComponentsInChildren<Toggle>());
        toggles.AddRange(roomToggle.GetComponentsInChildren<Toggle>());
        toggles.AddRange(weaponToggle.GetComponentsInChildren<Toggle>());

        if (accuse)
        {
            roomToggle.gameObject.SetActive(true);
        } else
        {
            roomToggle.gameObject.SetActive(false);
        }

        foreach (Card card in game.deck)
        {
            toggles[card.id - 1].GetComponentInChildren<Text>().text = card.cardName;
            // Turn the text red if it was disproven
            if (!card.disproven)
            {
                toggles[card.id - 1].GetComponentInChildren<Text>().color = Color.black;
            } else
            {
                toggles[card.id - 1].GetComponentInChildren<Text>().color = new Color(139, 0, 0);
            }
        }

        submitButton.onClick.RemoveAllListeners();
        submitButton.onClick.AddListener(() =>
        {
        if (accuse)
        {
            nm.Accuse(true,
                game.GetCard(toggles.FindIndex(i => i == suspectToggle.ActiveToggles().First()) + 1),
                game.GetCard(toggles.FindIndex(i => i == weaponToggle.ActiveToggles().First()) + 1),
                game.GetCard(toggles.FindIndex(i => i == roomToggle.ActiveToggles().First()) + 1));
                suggestUI.SetActive(false);
            } else
            {
                nm.SubmitMove(location,
                    game.GetCard(toggles.FindIndex(i => i == suspectToggle.ActiveToggles().First()) + 1),
                    game.GetCard(toggles.FindIndex(i => i == weaponToggle.ActiveToggles().First()) + 1),
                    location);
                    // game.GetCard(toggles.FindIndex(i => i == roomToggle.ActiveToggles().First()) + 1));
                suggestUI.SetActive(false);

            }
        });
    }

    public void AccuseQuestion()
    {
        accusePromptUI.SetActive(true);
        Location location = GameObject.Find("GameManager").GetComponent<Game>().player.character.location;
        yesAccuseButton.onClick.RemoveAllListeners();
        yesAccuseButton.onClick.AddListener(() => { 
            Suggest(location, true);
            accusePromptUI.SetActive(false);
        });
    }

    public void Disprove(List<Card> cards, Player player, int suggestingPlayer)
    {
        waitForTurnUI.SetActive(false);
        disproveUI.SetActive(true);

        int buttonIndex = 0;
        foreach (Card card in cards)
        {
            // Update label on this button and associate it with the proper card
            Button button = disproveButtons[buttonIndex];
            button.GetComponentInChildren<Text>().text = card.cardName;
            button.onClick.RemoveAllListeners();
            button.onClick.AddListener(() => {
                nm.Disprove(card, suggestingPlayer);
                disproveUI.SetActive(false);
            });
            button.interactable = true;

            // Button should only be interactable if the card is in our hand
            if (!player.hand.Contains(card))
            {
                button.interactable = false;
            }
            buttonIndex++;
        }
    }

    public void ShowCard(Card card, Character character)
    {
        // shownCardText.SetText(character.cardName + " showed you the " + card.cardName + " card.");
        card.cardObject.GetComponent<CardController>().Show();
    }

    public void SetName(Player player)
    {
        nameLabel.SetText(player.character.cardName);
        nameLabel.color = GameObject.Find(player.character.name)
            .GetComponent<MeshRenderer>().material.color;
    }

    public void Win()
    {
        winUI.SetActive(true);
        GameOver();
    }

    public void Lose()
    {
        loseUI.SetActive(true);
    }

    public void GameOver()
    {
        gameOverUI.SetActive(true);
    }

}
