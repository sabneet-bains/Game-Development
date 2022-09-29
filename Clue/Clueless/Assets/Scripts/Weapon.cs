using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * This script creates an inherited class called “Weapon” based on the “Card” class defined in “Card.cs” 
 * along with new constructors to define weapon movement and detailed animations.
 */

public class Weapon : Card
{

    public Vector3[] offsets;

    public void Move(Location location)
    {
        transform.position = location.transform.position + offsets[location.id - 7];
    }

}
