# Hunter and Gems

A fun and interactive game designed to introduce programming basics! Players guide a "hunter" across a board to collect gems by entering commands in a text box, simulating a programming environment.

## Table of Contents

- [Hunter and Gems](#hunter-and-gems)
  - [Table of Contents](#table-of-contents)
  - [Game Overview](#game-overview)
  - [Features](#features)
  - [Commands](#commands)
  - [Game Rules](#game-rules)
  - [Installation](#installation)
  - [License](#license)

## Game Overview

**Hunter and Gems** is a beginner-friendly game where players use coding-style commands to navigate a hunter and collect gems. It introduces concepts like syntax, logical thinking, and basic movement commands. The game is great for players new to programming, as it simulates a simplified coding environment.

## Features

- **Programming Simulation**: Players use programming-like commands to control the hunter
- **Syntax Practice**: Players learn about syntax by using commands to navigate the game
- **Level Progression**: The game includes multiple levels with different commands and strategies
- **Time Constraints**: Each level has a 2-minute timer to add challenge

## Commands

Players can use these commands to control the hunter:

- `move('up')`: Moves the hunter up one grid space
- `move('down')`: Moves the hunter down one grid space
- `move('left')`: Moves the hunter left one grid space
- `move('right')`: Moves the hunter right one grid space

Each command should be on a new line. Syntax must be accurate.

## Game Rules

1. Collect all gems by moving the hunter
2. Enter movement commands in the text box
3. Click **Submit Moves** to execute commands
4. Complete level by collecting all gems
5. 2-minute time limit per level

**Tips:**

- Use exact syntax (e.g., `move('up')`)
- Chain multiple commands together
- Check command accuracy

## Installation

1. Clone repository:

```bash
git clone https://github.com/dineshchhantyal/codeclash
cd codeclash
```

2. Install Flask:

```bash
pip install -r requirements.txt
```

3. Run application:

```bash
python app.py
```

4. Access game at http://127.0.0.1:5000

## License

This project is licensed under the MIT License.
