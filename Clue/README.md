<div align="center"><a name="readme-top"></a>

# 🧩 Clueless — A 3D Unity Adaptation of *Clue®* for Simulation & Systems Research

[![Unity](https://img.shields.io/badge/Unity-2021.1.6f1-555555?logo=unity&logoColor=white&labelColor=0d1117&style=flat)](https://unity.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-528ec5?logo=python&logoColor=white&labelColor=0d1117&style=flat)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-f29111?logo=mysql&logoColor=white&labelColor=0d1117&style=flat)](https://www.mysql.com/)
[![AWS](https://img.shields.io/badge/AWS-EC2%2FLightsail-FF9900?logo=amazonaws&logoColor=white&labelColor=0d1117&style=flat)](https://aws.amazon.com/)
[![3D Simulation](https://img.shields.io/badge/Domain-3D_Simulation-lightgrey?logo=unrealengine&logoColor=white&labelColor=0d1117&style=flat)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ECC71?labelColor=0d1117&style=flat)](https://choosealicense.com/licenses/mit/)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sabneet-bains/Game-Development/tree/main/Clue)

**A networked re-imagining of Clue® built for systems research and simulation studies.**  
<sup>*Integrating Unity (C#), Python (Flask), and MySQL in a distributed, multiplayer environment hosted via AWS.*</sup>

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/Game_Logo.png" alt="Clueless Logo" width="300" height="300">

</div>

> [!NOTE]
> <sup>This repository contains Unity-specific and Python networking code created for a course-level simulation systems project.  
> It is provided for research, reproducibility, and educational adaptation.</sup>


## 🧭 Table of Contents
- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Development Environment](#-development-environment)
- [How to Play](#-how-to-play)
- [Project Highlights](#-project-highlights)
- [Testing Setup](#-testing-setup)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)


## 🧠 Overview
**Clueless** is a 3D Unity-based adaptation of *Clue®*, developed as a **distributed multiplayer simulation** for exploring system design, AI logic, and database-driven game coordination.  
It demonstrates an end-to-end architecture integrating **C# gameplay**, **Python networking**, **MySQL persistence**, and **AWS deployment** — bridging entertainment software and research simulation systems.

> [!TIP]
> Built originally as an **academic capstone** under simulation and systems coursework — emphasizing real-time state management and modular design.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 📂 Repository Structure
````text
Clue/
│
├── Assets/
│   ├── Scripts/
│   │   ├── PlayerController.cs
│   │   ├── NetworkManager.cs
│   │   └── GameLogic.cs
│   ├── Scenes/
│   │   ├── GameBoard.unity
│   │   └── Lobby.unity
│   ├── Models/
│   │   ├── Cards/
│   │   └── Characters/
│   ├── Textures/
│   └── UI/
│
├── PythonServer/
│   ├── network_service.py
│   ├── db_connect.py
│   ├── create_tables.sql
│   └── requirements.txt
│
└── README.md
````

> [!TIP]
> Folder layout separates **Unity client (C#)** and **Python server (Flask/MySQL)** for modularity and scalability.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 💻 Development Environment

| Component | Tools & Versions | Purpose / Usage |
|:-----------|:----------------|:----------------|
| **Game Engine** | **Unity 2021.1.6f1** | Core 3D engine for gameplay, scene rendering, and physics logic. |
| **Programming IDEs** | **Visual Studio (C#)**, **VS Code (Python)** | Visual Studio for Unity scripting and debugging; VS Code for backend and server-side Python development. |
| **Languages & Frameworks** | **C#**, **Python 3.9+**, **Flask**, **MySQL 8.0** | Full-stack architecture for gameplay logic, networking, and database persistence. |
| **Backend Infrastructure** | **AWS EC2 / Lightsail** | Hosts multiplayer Flask server and MySQL database for networked gameplay. |
| **Version Control** | **Git** + optional **Git LFS** | Source and asset versioning for Unity scenes, scripts, and models. |
| **3D Modeling** | **Blender 2.9x+** | Creation and rigging of 3D characters, environments, and props. |
| **Texture & Image Editing** | **Adobe Photoshop (CC)** or **GIMP/Krita** | Texture design, UI assets, and visual polish for Unity integration. |
| **Vector & UI Design** | **Microsoft PowerPoint (SVG Export)** or **Inkscape** | Designed in-game cards, icons, and interface overlays for *Clueless*. |
| **Presentation & Planning** | **PowerPoint / Figma / Google Slides** | Used for mockups, gameplay flow diagrams, and presentation materials. |
| **Database Tools** | **MySQL Workbench**, **AWS RDS Console** | Schema visualization, table debugging, and remote database management. |
| **Build & Compilation** | **.NET Build Tools**, **C# Compiler**, **Unity Hub** | Required for Unity builds, project packaging, and dependency management. |
| **Project Management** | **GitHub**, **AWS Console**, **Unity Collaborate (legacy)** | Repository organization, deployment control, and task management. |

> [!TIP]
> Cloud-hosted sessions were managed through an **AWS Flask backend**, linking Unity clients with a **MySQL database** to enable multiplayer coordination and synchronized game states across distributed players.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>

## 🕹️ How to Play

**Clueless** reimagines *Clue®* as a fully 3D, networked Unity simulation connected to a Python/MySQL backend.

1. Open the project in **Unity 2021.1.6f1** via **Unity Hub**.  
2. Ensure the **Python Flask server** is running locally or hosted on AWS.  
3. Launch the Unity game from the **Lobby** scene.  
4. Connect to the backend (default host: `localhost:50051`).  
5. Explore the mansion, investigate rooms, and submit hypotheses — just like the board game!  

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/game_title.gif" alt="Game Title" width="853.3" height="480">
<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/gameboard.gif" alt="Game Board" width="853.3" height="480">

> [!NOTE]
> Gameplay synchronization and turn-order logic are handled by the **Flask server**, ensuring real-time state management across all connected players.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🔬 Project Highlights

| Feature | Description |
|:--------|:-------------|
| **3D Game Engine (Unity)** | Built using Unity’s physics and animation systems for immersive gameplay. |
| **Networking Layer (Flask + MySQL)** | Manages session control, player communication, and synchronized updates. |
| **AWS Deployment** | Hosted on **AWS EC2/Lightsail**, enabling persistent multiplayer connectivity. |
| **Cross-Language Architecture** | Combines Unity (C# client) with Python (Flask backend) for distributed logic. |
| **Database-Driven Gameplay** | MySQL tables store players, sessions, and clues, ensuring data consistency. |
| **UI & Asset Workflow** | Custom 3D cards and interface assets designed in **Blender**, **Photoshop**, and **PowerPoint (SVG)**. |
| **Research Orientation** | Serves as a sandbox for studying **network synchronization**, **simulation scaling**, and **systems design**. |

> [!TIP]
> Designed for **academic reproducibility** — gameplay systems can be adapted to study distributed logic, server latency, and multiplayer coordination frameworks.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🧪 Testing Setup
````bash
# 1. Install and configure MySQL
mysql -u root -p
CREATE DATABASE clueless;
GRANT ALL PRIVILEGES ON *.* TO 'clueless'@'localhost' IDENTIFIED BY 'Password1';

# 2. Load schema from SQL script
mysql -u clueless -p clueless < create_tables.sql

# 3. Python environment setup
pip install -r requirements.txt

# 4. Run Flask server (local or AWS)
python3 network_service.py

# 5. Configure Unity client
# In NetworkManager.cs, set the backend host (default: localhost:50051)
````
> [!IMPORTANT]
> When deploying on **AWS**, update the **Flask server IP** and **database credentials** in Unity’s network configuration script to enable remote connections.  
> MySQL security groups and inbound rules must allow external connections on the proper port (default: **3306**).  
> For best stability, configure **Flask** with `threaded=True` and use a **persistent connection pool** for MySQL.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## ⚙️ Requirements
````text
Unity Editor 2021.1.6f1
Visual Studio (C# Build Tools + .NET SDK)
Python >= 3.9
Flask >= 2.0
MySQL >= 8.0
Git + Git LFS
Blender 2.9x+
Photoshop (or GIMP/Krita)
PowerPoint (or Inkscape for SVG export)
AWS CLI (for deployment)
MySQL Workbench (optional)
````

> [!IMPORTANT]
> Ensure **.NET SDK**, **Python**, and **Unity build tools** are installed and compatible.  
> For multiplayer hosting, configure **AWS Flask server** credentials and **MySQL** connection strings.

<div align="right">

[![Back to Top](https://img.shields.io/badge/-⫛_TO_TOP-0d1117?style=flat)](#readme-top)

</div>


## 🤝 Contributing
**Contributions are welcome!**

1. **Open an issue** to discuss architectural or gameplay changes.  
2. **Follow established conventions** (Unity C# / Python PEP-8).  
3. **Document updates** — including schema, logic flow, or UI enhancements.  
4. **Submit a pull request** for review and merge.

> [!TIP]
> High-impact contributions include **AI-driven logic**, **network optimization**, and **backend scaling** for larger multiplayer environments.

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

<sub>“Systems games remind us — complexity can be playful when order emerges from design.”</sub>

</div>
