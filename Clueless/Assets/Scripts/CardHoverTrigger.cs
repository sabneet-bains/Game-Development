using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CardHoverTrigger : MonoBehaviour
{


    /*
     *  When the mouse hovers over this trigger, reveal the cards in your hand
     */
    private void OnMouseEnter()
    {
        CardController.RevealHand();
    }

    /*
     * When the mouse leaves this trigger, stow the cards in your hand
     */
    private void OnMouseExit()
    {
        CardController.StowHand();
    }
}
