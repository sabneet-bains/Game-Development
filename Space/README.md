# Space Ball - A planetary basketball game?

Space Ball is a Python-based simulation game that combines planetary motion and basketball. The game uses VPython 7 for its graphical physics simulation.


![](https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball.gif)

→ `In a transition from VPython 6 to 7, some of the game logic is finicky – may be fixed at a later stage.`

## Requirements

[Python 3.9.1 or later (64-bit)](https://www.python.org/downloads/)

[VPython 7](https://vpython.org/presentation2018/install.html)

## Build Tested

Visual Studio Code
* Version: 1.52.1 (system setup)
* Commit: ea3859d4ba2f3e577a159bc91e3074c5d85c0523
* Electron: 9.3.5
* Chrome: 83.0.4103.122
* Node.js: 12.14.1
* V8: 8.3.110.13-electron.0
* OS: Windows_NT x64 10.0.19042
* Memory: 1981M
* Cores: 8

Microsoft Edge
* Version 89.0.767.0 (Official build) dev (64-bit)

## How to Play

1)	Open the project in **Visual Studio Code** > _run_ the Game_Engine.py

```python
from vpython import *
import numpy
import random
#--------------------------------Constants-------------------------------------

G = 6.67e-11
RP = 6.378e6
MP = 5.972e24
gravity = -9.8

#----------------------------------Scene---------------------------------------

scene = canvas(title = 'Space Basketball', width = 1688, height = 800,
    center = vector(0, 0, 3*RP), range = 4*RP, autoscale = True)

scene.camera.pos = vector(4*RP, 0, 8*RP)
scene.lights = []

    ..
    ...
    ....

```

2)	The game will open in a new browser window:

![](https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball_Intro.png)

3)	Provide game parameters such as the ball's initial angle, velocity, and even absurd gravity, and start playing!

![](https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball2.png)

## Contributing

If you would like to contribute to this repository, please follow these guidelines:

* Create an issue to discuss the changes you would like to make
* Fork the repository and make the changes
* Submit a pull request for review and merging
* Please make sure to update tests as appropriate

## License
This repository is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
