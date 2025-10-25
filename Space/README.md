# 🪐 Space Ball — A Planetary Basketball Game
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![VPython](https://img.shields.io/badge/VPython-7.0-red?logo=visualstudio&logoColor=white)](https://vpython.org/)
[![Physics Simulation](https://img.shields.io/badge/Engine-Physics_Simulation-lightgrey?logo=atom&logoColor=white)](#)
[![3D Visualization](https://img.shields.io/badge/3D-Visualization-orange?logo=googleearth&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

<br>

**Space Ball** is a Python-based simulation game that blends *orbital mechanics* and *basketball physics*.  
Built with **VPython 7**, it visualizes gravitational motion and interactive gameplay in a real-time 3D environment.

![](https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball.gif)

> ⚙️ *Some gameplay logic requires tuning after migration from VPython 6 → 7. Future updates may address compatibility and stability.*



## 📦 Requirements

- [Python 3.9.1 or later (64-bit)](https://www.python.org/downloads/)
- [VPython 7](https://vpython.org/presentation2018/install.html)



## 💻 Development Environment

<details>
<summary>Click to expand</summary>

**Visual Studio Code**
- Version 1.52.1 (system setup)
- Commit ea3859d4ba2f3e577a159bc91e3074c5d85c0523  
- Electron 9.3.5 • Chrome 83.0.4103.122 • Node.js 12.14.1 • V8 8.3.110.13-electron.0  
- OS Windows_NT x64 10.0.19042  
- Memory 1981 MB • Cores 8  

**Microsoft Edge**
- Version 89.0.767.0 (Official build) Dev (64-bit)

</details>



## 🪐 How to Play

#### **1.** Open the project in **Visual Studio Code** and run `Game_Engine.py`.

```python
from vpython import *
import numpy
import random

#--------------------------------Constants-------------------------------------
G  = 6.67e-11
RP = 6.378e6
MP = 5.972e24
gravity = -9.8

#----------------------------------Scene---------------------------------------
scene = canvas(title='Space Basketball', width=1688, height=800,
               center=vector(0, 0, 3*RP), range=4*RP, autoscale=True)
scene.camera.pos = vector(4*RP, 0, 8*RP)
scene.lights = []

# ... gameplay logic ...
```

#### **2.** A browser window will open automatically:  
![](https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball_Intro.png)

#### **3.** Enter launch parameters (angle, velocity, or even *custom gravity*) — then shoot for orbit!  
![](https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball2.png)



## 🔬 Tech Highlights

- **Physics Engine →** Newtonian gravity, orbital motion, and parametric projectile paths.  
- **Gameplay Logic →** Real-time motion under variable G and launch angles.  
- **Visualization →** Interactive 3-D scene with dynamic camera control and lighting.  
- **Extensibility →** Easily tune constants, masses, and interaction rules for new modes.


## 🤝 Contributing

Physicists, coders, and simulation enthusiasts are welcome!

1. Open an issue to discuss ideas or proposed changes.  
2. Fork the repository and make your improvements.  
3. Submit a pull request for review and merging.  
4. Update or add tests where appropriate.

> 💡 Contributors curious about **physics-based gameplay**, **VPython optimization**, or **simulation R&D** are especially encouraged to join.


## 🧠 Author

**Sabneet Bains** — *Quantum × AI × Scientific Computing*  
[LinkedIn](https://www.linkedin.com/in/sabneet-bains/) • [GitHub](https://github.com/sabneet-bains)


## 📄 License

This repository is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

