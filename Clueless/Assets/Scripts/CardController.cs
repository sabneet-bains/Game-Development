using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CardController : MonoBehaviour
{
    private static float nextHandPos = 0;
    private static float nextOffset = 2.5f;
    private static HashSet<CardController> hand = new HashSet<CardController>();

    public Animator animator;
    private float distanceFromView = 8.0f;

    public void AddToHand()
    {
        Center();

        Debug.Log(nextHandPos);
        // Shift the card down by a fixed amount, and offset depending on number in hand
        transform.Translate(new Vector3(nextHandPos, -5, 0), Space.Self);

        // Add this card to the hand
        hand.Add(this);

        // Animate dealing the card
        animator.SetTrigger("TDeal");

        // Update the x position for the next card in the hand
        nextHandPos += nextOffset;
        nextOffset = -System.Math.Sign(nextHandPos) * (System.Math.Abs(nextOffset) + 2.5f);
    }

    // Position the card in the middle of the view and rotate it to face the camera
    private void Center()
    {
        // Get the worldspace coordinates a few meters from the camera along frustum midpoint
        Vector3 viewportCenter = Camera.main.ViewportToWorldPoint(new Vector3(0.5f, 0.5f, distanceFromView));
        transform.position = viewportCenter;

        // Rotate the card to face the camera
        transform.rotation = Camera.main.transform.rotation;
    }

    public void Reveal()
    {
        animator.SetTrigger("TReveal");
    }

    public void Show()
    {
        // Place the card slightly off to the right
        Center();
        transform.Translate(new Vector3(16.5f, 0, 0), Space.Self);

        // Rotate it so it faces away
        transform.Rotate(0, 180, 0, Space.Self);

        // Show the card with the Show animation
        animator.SetTrigger("TShow");
    }

    public void Stow()
    {
        animator.SetTrigger("TStow");
    }

    public static void RevealHand()
    {
        foreach(CardController card in hand)
        {
            card.Reveal();
        }
    }

    public static void StowHand()
    {
        foreach (CardController card in hand)
        {
            card.Stow();
        }
    }
}
