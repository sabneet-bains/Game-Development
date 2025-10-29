<div align="center"><a name="readme-top"></a>

# 🎮 Game Development — Interactive Physics & Simulation Worlds

[![Python](https://img.shields.io/badge/Python-3.9%2B-528ec5?logo=python&logoColor=white&labelColor=0d1117&style=flat)](https://www.python.org/)
[![Unity](https://img.shields.io/badge/Unity-2021.1.6f1-555555?logo=unity&logoColor=white&labelColor=0d1117&style=flat)](https://unity.com/)
[![VPython](https://img.shields.io/badge/VPython-7.0-8e44ad?logo=python&logoColor=white&labelColor=0d1117&style=flat)](https://vpython.org/)
[![3D Simulation](https://img.shields.io/badge/Domain-3D_Simulation-lightgrey?logo=unrealengine&logoColor=white&labelColor=0d1117&style=flat)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ECC71?labelColor=0d1117&style=flat)](https://choosealicense.com/licenses/mit/)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sabneet-bains/Game-Development)

**When physics meets play.**  
<sup>*A fusion of game logic, physical simulation, and creative visualization — bridging entertainment and computational modeling.*</sup>

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/gameboard.gif" alt="Clue 3D Gameboard" width="853.3" height="480">

</div>

> [!NOTE]
> <sup>Part of the <b>Foundational & Academic</b> collection — educational tools designed with engineering rigor.</sup>


## 🧭 Table of Contents
- [Overview](#-overview)
- [Featured Projects](#-featured-projects)
- [Repository Structure](#-repository-structure)
- [Development Environment](#-development-environment)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)


## 🧠 Overview
This repository showcases a curated selection of **interactive 3D games** and **physics-driven simulations** developed using **Unity (C#)** and **VPython (Python)**.  
Each project merges **gameplay logic** with **scientific principles**, demonstrating how classical mechanics, AI-driven decision systems, and visualization pipelines can coexist within playful, research-driven environments.

> [!TIP]
> Ideal for exploring **simulation-based learning**, **procedural design**, and **hybrid AI–physics modeling**.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🕹️ Featured Projects

| 🧩 Project | 🧮 Description | 🧠 Engine / Language |
|:-----------|:---------------|:--------------------|
| 🎲 **Clueless (Unity 3D)** | A 3D adaptation of *Clue®*, featuring C# gameplay scripts and a Python–MySQL backend for multiplayer coordination. | Unity + Python |
| 🪐 **SpaceBall (VPython)** | A planetary basketball simulation combining orbital dynamics and gameplay physics. | Python (VPython) |

> [!NOTE]
> Each project pairs **creative game design** with **computational modeling** — serving both entertainment and educational goals.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 📂 Repository Structure
````text
Game-Development/
│
├── Clue/
│   ├── Assets/
│   │   ├── Scripts/
│   │   ├── Scenes/
│   │   └── Models/
│   ├── PythonServer/
│   │   ├── db_connect.py
│   │   └── multiplayer.py
│   └── Clueless.sln
│
├── Space/
│   ├── SpaceBall.py
│   ├── physics_utils.py
│   └── textures/
│
└── README.md
````

> [!TIP]
> Folder layout mirrors **game × simulation** structure — Unity projects and VPython simulations coexist for modular cross-study.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 💻 Development Environment

| Component | Tools & Versions | Purpose / Usage |
|:-----------|:----------------|:----------------|
| **Game Engine** | **Unity 2021.1.6f1** | Core 3D engine for *Clueless* gameplay logic, physics, and user interface. |
| **Programming IDEs** | **Visual Studio (C#)**, **VS Code (Python)** | Visual Studio for Unity scripting and debugging; VS Code for VPython server and utilities. |
| **Languages & Frameworks** | **C#**, **Python 3.9+**, **VPython 7**, **.NET SDK** | Core development stack spanning gameplay systems, networking, and simulation. |
| **Backend Infrastructure** | **AWS EC2 / Lightsail**, **Python Flask Server**, **MySQL** | Cloud-hosted multiplayer backend handling player sessions, database queries, and game state synchronization. |
| **Version Control** | **Git** + optional **Git LFS** | Project management, source tracking, and large-asset versioning (models, textures, binaries). |
| **3D Modeling** | **Blender 2.9x+** | Creation, rigging, and animation of characters, props, and environments for Unity import. |
| **Texture & Image Editing** | **Adobe Photoshop (CC)** or **GIMP/Krita** | Texture and material design for 3D models and UI elements. |
| **Vector & UI Design** | **Microsoft PowerPoint (SVG Export)** or **Inkscape** | Designed custom card sets, icons, and vector overlays for *Clueless*’s interface. |
| **Presentation & Layout Planning** | **PowerPoint / Figma / Google Slides** | Mockups, flow diagrams, and gameplay UX visualization. |
| **Physics Simulation** | **VPython 7**, optional **GlowScript** | Used in *SpaceBall* for real-time planetary motion and physics visualization. |
| **Server Layer (SpaceBall)** | **Python 3.9+**, `Flask` or `http.server` | Lightweight local or web server for simulation telemetry and visualization. |
| **Asset Pipeline** | **Unity Importer**, **Blender FBX/GLB Export** | Converts 3D and 2D assets for integration into Unity. |
| **Build & Compilation** | **.NET Build Tools**, **C# Compiler**, **Unity Hub** | Required for building Unity assemblies, managing dependencies, and packaging games. |
| **Project Management** | **GitHub**, **AWS Console**, **Unity Collaborate (legacy)** | Coordination of commits, deployment management, and repository organization. |

> [!TIP]
> Cloud-hosted play sessions were supported via an **AWS Flask server**, linking Unity C# clients to a **Python + MySQL backend** — enabling real-time multiplayer coordination and persistent state management.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## ⚙️ Requirements
````text
Unity Editor 2021.1.6f1
Visual Studio (C# Build Tools + .NET SDK)
Python >= 3.9
vpython >= 7.0
Flask >= 2.0
MySQL (local or AWS RDS)
Git + Git LFS
Blender 2.9x+
Photoshop (or GIMP/Krita)
PowerPoint (or Inkscape for SVG export)
AWS CLI (for deployment)
````

> [!IMPORTANT]
> Ensure **.NET SDK**, **Python**, and **Unity build tools** are installed and compatible.  
> For multiplayer hosting, configure **AWS Flask server** credentials and **MySQL** connection strings.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🤝 Contributing
**Contributions are welcome!**  
To maintain a structured and reproducible development flow:

1. **Open an issue** before major gameplay or physics changes.  
2. **Follow project conventions** (Unity C# style / PEP-8 for Python).  
3. **Add reproducibility artifacts** — screenshots, logs, or short demos.  
4. **Submit a pull request** with clear change rationale and validation steps.

> [!TIP]
> High-value additions include **AI-driven mechanics**, **cloud-based multiplayer scaling**, and **real-time physics improvements**.

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

<sub>“Play is not the opposite of work — it’s the physics of imagination in motion.”</sub>

</div>
