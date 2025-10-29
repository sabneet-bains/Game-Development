<div align="center"><a name="readme-top"></a>

# 🪐 Space Ball — A Planetary Basketball Simulation

[![Python](https://img.shields.io/badge/Python-3.9%2B-528ec5?logo=python&logoColor=white&labelColor=0d1117&style=flat)](https://www.python.org/)
[![VPython](https://img.shields.io/badge/VPython-7.0-c0392b?logo=visualstudio&logoColor=white&labelColor=0d1117&style=flat)](https://vpython.org/)
[![Physics Simulation](https://img.shields.io/badge/Domain-Physics_Simulation-lightgrey?logo=atom&logoColor=white&labelColor=0d1117&style=flat)](#)
[![3D Visualization](https://img.shields.io/badge/3D-Visualization-f39c12?logo=googleearth&logoColor=white&labelColor=0d1117&style=flat)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ECC71?labelColor=0d1117&style=flat)](https://choosealicense.com/licenses/mit/)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sabneet-bains/Game-Development/tree/main/Space)

**When gravity meets gameplay.**  
<sup>*A planetary-scale basketball simulation blending orbital mechanics and interactive 3D visualization — built with VPython 7.*</sup>

<img src="https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball.gif" alt="Space Ball Gameplay" width="853.3" height="480">

</div>

> [!NOTE]
> <sup>Originally developed as part of the *Game Development* and *Scientific Visualization* series — demonstrating simulation-based learning through interactive physics systems.</sup>


## 🧭 Table of Contents
- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Development Environment](#-development-environment)
- [How to Play](#-how-to-play)
- [Tech Highlights](#-tech-highlights)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)


## 🧠 Overview
**Space Ball** simulates the physics of a basketball game set in outer space — where players launch projectiles into planetary orbit under real gravitational parameters.  
Developed in **Python 3.9+** using **VPython 7**, it visualizes Newtonian dynamics in real time, creating a playful yet educational environment for studying **orbital motion**, **energy conservation**, and **parametric projectile dynamics**.

> [!TIP]
> Serves as both a **teaching aid** in physics courses and a **sandbox** for testing gameplay mechanics grounded in scientific modeling.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 📂 Repository Structure
````text
Space/
│
├── SpaceBall.py
├── physics_utils.py
├── Space_Ball.gif
├── Space_Ball2.png
├── Space_Ball_Intro.png
└── README.md
````

> [!TIP]
> Code is modular — physics constants, rendering parameters, and gameplay logic can be edited independently for custom experiments.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 💻 Development Environment

| Component | Tools & Versions | Purpose / Usage |
|:-----------|:----------------|:----------------|
| **Programming Language** | **Python 3.9+ (64-bit)** | Core language for simulation logic and gameplay computation. |
| **Simulation Framework** | **VPython 7.0** | Provides real-time 3D visualization and physics rendering. |
| **IDE** | **Visual Studio Code** | Primary environment for writing, debugging, and running scripts. |
| **Browser Renderer** | **GlowScript (via VPython)** | Web-based 3D rendering when hosted or executed in notebook mode. |
| **Graphics Engine** | **OpenGL (through VPython)** | Handles camera, lighting, and scene composition. |
| **Version Control** | **Git / GitHub** | Tracks simulation versions, experiments, and assets. |
| **Optional Tools** | **Blender**, **Photoshop / GIMP** | Used for visual design, textures, and educational overlays. |

> [!NOTE]
> Certain constants were re-tuned during the **VPython 6 → 7 migration** to maintain accurate real-time physics and rendering stability.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🪐 How to Play

1. Open the project in **Visual Studio Code** (or another Python IDE).  
2. Run the main file:  
   ```bash
   python SpaceBall.py
   ```  
3. A VPython or browser window will open automatically.  
4. Adjust launch parameters (velocity, angle, or gravity) and shoot for orbit!  
5. Observe trajectories as gravitational constants or mass values are modified.

<img src="https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball_Intro.png" alt="Intro Scene" width="853.3" height="480">
<img src="https://github.com/sabneet95/Game-Development/blob/main/Space/Space_Ball2.png" alt="Gameplay View" width="853.3" height="480">

> [!TIP]
> Experiment with **planetary mass (MP)** and **gravitational constant (G)** to visualize orbital stability, free-fall, and escape velocity thresholds.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🔬 Tech Highlights

| Feature | Description |
|:--------|:-------------|
| **Physics Engine** | Implements Newtonian gravity and projectile motion equations. |
| **Gameplay Logic** | Real-time parametric control of launch vectors and energy dynamics. |
| **Visualization** | 3D interactive camera and dynamic lighting built in VPython. |
| **Parametric Inputs** | User-adjustable parameters for angle, force, and gravitational strength. |
| **Educational Focus** | Demonstrates classical mechanics through gamified visualization. |
| **Extensibility** | Supports modifications for orbital mechanics, collisions, or AI opponents. |

> [!TIP]
> Designed as an **educational playground** for studying **mechanics**, **momentum conservation**, and **orbital trajectories** through interactive experimentation.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## ⚙️ Requirements
````text
Python >= 3.9
vpython >= 7.0
numpy >= 1.24
````

> [!IMPORTANT]
> VPython requires an active browser or compatible 3D rendering environment.  
> Use a modern browser (Edge, Chrome, or Firefox) and enable **hardware acceleration** for smooth visualization.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🤝 Contributing
**Contributions are welcome!**

1. **Open an issue** to suggest physics enhancements or gameplay ideas.  
2. **Fork** the repository and implement improvements.  
3. **Document results** — include comparisons, graphs, or screenshots.  
4. **Submit a pull request** for review and discussion.

> [!TIP]
> Potential extensions include **multi-body gravitation**, **AI-assisted aiming**, or **VR-enabled visualization** using WebVPython.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


<div align="center">

##
### 👤 Author  
**Sabneet Bains**  
*Quantum × AI × Scientific Computing*  
[LinkedIn](https://www.linkedin.com/in/sabneet-bains/) • [GitHub](https://github.com/sabneet-bains)

##
### 📄 License  
Licensed under the [MIT License](https://choosealicense.com/licenses/mit/)

<sub>“Gravity is not a force that pulls us down — it’s the rhythm that keeps the game in motion.”</sub>

</div>
