# Clueless: A 3D Unity Game

A repository of a 3D Unity implementation of the popular board game Clue® for academic purposes!

<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/Game_Logo.png" width="300" height="300">

→ `Domain-specific code! Will not work on its own but can be modified for other projects.`

## Requirements

[Unity 2021.1.6f1](https://unity3d.com/unity/whats-new/2021.1.6)

## Build Environment

This code has been tested on the following setup:

* Visual Studio Code: 1.52.1
* Electron: 9.3.5
* Chrome: 83.0.4103.122
* Node.js: 12.14.1
* V8: 8.3.110.13-electron.0
* Operating System: Windows 11 (64-bit)
* Memory: 1981 MB
* Cores: 8

## How to Play

1)	Open the project in **Unity** > and install any required extensions


<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/game_title.gif" width="853.3" height="480">


2)  Game away!


<img src="https://github.com/sabneet95/Game-Development/blob/main/Clue/gameboard.gif" width="853.3" height="480">

## Contributing

If you would like to contribute to this repository, please follow these guidelines:

* Create an issue to discuss the changes you would like to make
* Fork the repository and make the changes
* Submit a pull request for review and merging
* Please make sure to update tests as appropriate

## Testing Setup

To set up the game for testing, follow these steps:

1. Install MySQL on your system from here.
2. Connect to MySQL as the root user: mysql -u root -p.
3. Create the Clueless database: CREATE DATABASE clueless;.
4. Add the Clueless application MySQL user: GRANT ALL PRIVILEGES ON *.* TO 'clueless'@'localhost' IDENTIFIED BY 'Password1';.
5. Create all of the tables by running the commands from create_tables.sql.
6. Install Python 3 and pip. A virtual environment is recommended.
7. Install the Python requirements: pip install -r requirements.txt.
8. If there are any issues, it is likely due to MySQL. Please let the developers know if additional support is needed.
9. Run the server: python3 network_service.py.
10. In the Unity NetworkManager class, set the host to localhost:50051.
11. You should be good to go! Everything will run locally.

## License
This repository is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
