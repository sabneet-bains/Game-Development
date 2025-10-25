# 🧩 Clueless — A 3D Unity Adaptation of Clue® for Simulation & Systems Research  

[![Unity](https://img.shields.io/badge/Unity-2021.1.6f1-black?logo=unity)](https://unity.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)](https://www.mysql.com/)
[![3D Game Engine](https://img.shields.io/badge/Engine-3D_Simulation-lightgrey?logo=unrealengine&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

---

**Clueless** is a Unity-based re-imagining of the classic board game *Clue®*, built as a 3D networked simulation for academic and research exploration.  

The project integrates **C# game logic**, **Python/MySQL networking**, and **Unity 3D visualization** to demonstrate systems-level interaction in a distributed game environment.

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/Game_Logo.png" width="300" height="300">

> 🧠 *Note: This repository contains domain-specific Unity code developed for a course environment.  
It may not run standalone, but can be adapted for similar systems or teaching projects.*

---

## 📦 Requirements

- [Unity 2021.1.6f1](https://unity3d.com/unity/whats-new/2021.1.6)

---

## 💻 Development Environment

<details>
<summary>Click to expand</summary>

**Visual Studio Code**
- Version 1.52.1  
- Electron 9.3.5  
- Chrome 83.0.4103.122  
- Node.js 12.14.1  
- V8 8.3.110.13-electron.0  

**System**
- OS: Windows 11 (64-bit)  
- Memory: 1981 MB  
- Cores: 8  

</details>

---

## 🕹️ How to Play

**This project reimagines Clue® as a 3D Unity networked simulation with a MySQL backend.**

1️⃣ Open the project in **Unity** and install any required extensions.  

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/game_title.gif" width="853.3" height="480">

2️⃣ Launch the game and explore!  

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/gameboard.gif" width="853.3" height="480">

---

## 🔬 Project Highlights

- **3D Game Engine →** Developed in Unity 2021 with optimized C# gameplay scripts.  
- **Networking Layer →** Python + MySQL backend enabling multiplayer coordination.  
- **Systems Integration →** Hybrid Unity–Python architecture with database-driven state updates.  
- **Research Context →** Built for game AI / simulation systems coursework under agile iteration.  

---

## 🧪 Testing Setup

<details>
<summary>Click to expand detailed setup</summary>

1. Install **MySQL** on your system.  
2. Connect as root:  
   ```bash
   mysql -u root -p
   ```  
3. Create the database:  
   ```sql
   CREATE DATABASE clueless;
   ```  
4. Add the application user:  
   ```sql
   GRANT ALL PRIVILEGES ON *.* TO 'clueless'@'localhost' IDENTIFIED BY 'Password1';
   ```  
5. Create tables by running commands from `create_tables.sql`.  
6. Install **Python 3** and `pip` (virtual environment recommended).  
7. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```  
8. If issues occur, check your MySQL configuration.  
9. Run the server:  
   ```bash
   python3 network_service.py
   ```  
10. In Unity’s **NetworkManager** class, set the host to `localhost:50051`.  
11. ✅ Everything should now run locally.

</details>

---

## 🤝 Contributing

Contributions are welcome!

1. Open an issue to discuss proposed changes.  
2. Fork the repository and make your improvements.  
3. Submit a pull request for review and merging.  
4. Update or add tests where appropriate.  

> 💡 Contributors interested in **Unity simulation**, **networked gameplay**, or **Python–MySQL integration** are especially encouraged to collaborate.

---

## 🧠 Author

**Sabneet Bains** — *Quantum × AI × Scientific Computing*  
[LinkedIn](https://www.linkedin.com/in/sabneet-bains/) • [GitHub](https://github.com/sabneet-bains)

---

## 📄 License

This repository is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---
