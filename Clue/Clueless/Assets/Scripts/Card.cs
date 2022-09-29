using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

/**
 * This script creates an inherited class called “Card” based on the base unity “MonoBehaviour” class
 */

public class Card : MonoBehaviour
{
    // These have all been passed in using the Unity UI, they don't need to be constructed
    public int id;
    public string cardName;
    public bool disproven;
    public GameObject cardObject;
    public TextMeshProUGUI notebookEntry;

    // Start is called before the first frame update
    public virtual void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void Disprove()
    {
        disproven = true;
        notebookEntry.fontStyle = FontStyles.Strikethrough;
    }
}
