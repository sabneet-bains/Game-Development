using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * This script creates an inherited class called “Character” based on the “Card” class defined in “Card.cs” 
 * along with new constructors to define character movement and detailed animations.
 */

public class Character : Card
{
    public Location location;
    public Vector3 locationOffset; // So they won't overlap when in the same room
    public Vector3[] offsets;
    private float speed = 3f;
    public Vector3 dest;
    public Vector3 start;

    public override void Start()
    {
        base.Start();

        // Move the character to their starting location at the beginning of the game
        Move(location);
    }

    public void Update()
    {
        var path = dest - this.location.transform.position;
        var lift = Vector3.up;
        if (transform.position != dest)
        {
            if (Vector3.Distance(start, transform.position) < 0.5 * Vector3.Distance(start, dest))
            {
                lift = 10*Vector3.up;
            }
            else
            {
                lift = Vector3.zero;
            }
            transform.position = Vector3.MoveTowards(transform.position, 
                dest + lift, 
                speed * Time.deltaTime);
        }
    }

    public void Move(Location location)
    {
        this.location = location;
        start = this.location.transform.position;
        if (location.id >= 0)
        {
            dest = location.transform.position + offsets[location.id - 7];
        } else
        {
            dest = location.transform.position + locationOffset;
        }
    }
}
