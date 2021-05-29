using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NotebookController : MonoBehaviour
{
    public GameObject notebook;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ShowHideNotebook()
    {
        notebook.SetActive(!notebook.activeSelf);
    }
}
