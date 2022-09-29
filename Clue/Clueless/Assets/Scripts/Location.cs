using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * This script creates an inherited class called “Location” based on the “Card” class defined in “Card.cs” 
 * along with a public method to check whether a hallway is blocked.
 */

public class Location : Card
{
    public List<Location> adjacent;

    public bool IsBlocked()
    {
        // Only hallways can be blocked; hallways have negative ids
        if (this.id >= 0)
        {
            return false;
        }

        // If any of the player characters are in this hall, it is blocked
        Game game = GameObject.Find("GameManager").GetComponent<Game>();
        foreach (Character character in game.pcs.Values) {
            if (character.location == this)
            {
                return true;
            }
        }

        // No one was in it, so it's unblocked
        return false;
    }
}
