using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * This script creates a new class called “Player” with member variables for player id, player name, 
 * player’s clue character, list of cards in hand, and location during the last turn.
 */

public class Player
{
    public int id;
    public string name;
    public Character character;
    public List<Card> hand;
    public Location lastTurnLocation = null;
    
    public Player(int id, string name, Character character)
    {
        this.id = id;
        this.name = name;
        this.character = character;
        hand = new List<Card>();
    }

    public void AddToHand(Card card)
    {
        this.hand.Add(card);
        card.Disprove();
    }

    public void AddToHand(ICollection<Card> cards)
    {
        foreach (Card card in cards)
        {
            AddToHand(card);
        }
    }

    public bool CardInHand(Card card)
    {
        return hand.Contains(card);
    }
}
