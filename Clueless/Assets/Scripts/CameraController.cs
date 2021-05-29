using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public Animator animator;
    public GameObject roomLabels;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            roomLabels.SetActive(true);
            animator.SetTrigger("Overhead");
        } else if (Input.GetKeyDown(KeyCode.Keypad8))
        {
            Ballroom();
        } else if (Input.GetKeyDown(KeyCode.Keypad2))
        {
            Hall();
        } else if (Input.GetKeyDown(KeyCode.Keypad5))
        {
            Billiard();
        } else if (Input.GetKeyDown(KeyCode.Keypad9))
        {
            Conservatory();
        } else if (Input.GetKeyDown(KeyCode.Keypad4))
        {
            Dining();
        } else if (Input.GetKeyDown(KeyCode.Keypad7))
        {
            Kitchen();
        } else if (Input.GetKeyDown(KeyCode.Keypad6))
        {
            Library();
        } else if (Input.GetKeyDown(KeyCode.Keypad1))
        {
            Lounge();
        } else if (Input.GetKeyDown(KeyCode.Keypad3))
        {
            Study();
        }
        else if (Input.GetKeyUp(KeyCode.Space))
        {
            roomLabels.SetActive(false);
            Default();
        }
    }

    public void ShowLocation(Card location)
    {
        switch (location.id)
        {
            case 14:
                Ballroom();
                break;
            case 7:
                Billiard();
                break;
            case 13:
                Conservatory();
                break;
            case 8:
                Dining();
                break;
            case 10:
                Hall();
                break;
            case 15:
                Kitchen();
                break;
            case 12:
                Library();
                break;
            case 9:
                Lounge();
                break;
            case 11:
                Study();
                break;
        }
    }

    public void Study()
    {
        animator.SetTrigger("Study");
    }

    public void Lounge()
    {
        animator.SetTrigger("Lounge");
    }

    public void Library()
    {
        animator.SetTrigger("Library");
    }

    public void Kitchen()
    {
        animator.SetTrigger("Kitchen");
    }

    public void Dining()
    {
        animator.SetTrigger("Dining");
    }

    public void Ballroom()
    {
        animator.SetTrigger("Ballroom");
    }

    public void Billiard()
    {
        animator.SetTrigger("Billiard");
    }

    public void Hall()
    {
        animator.SetTrigger("Hall");
    }

    public void Conservatory()
    {
        animator.SetTrigger("Conservatory");
    }

    public void Default()
    {
        animator.SetTrigger("Default");
    }
}
