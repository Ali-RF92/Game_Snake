# 🐍 Snake Game (Python + Pygame)

A simple Snake game built using **Python** and **Pygame**.
This project is part of my learning journey in game development and Python.

---

## 🎮 Features

* Classic Snake gameplay
* Real-time movement using keyboard (Arrow keys)
* Food generation system
* Score-based speed increase
* Maximum speed limit (12 FPS)
* Collision detection (self-collision)
* Game restart system after death

---

## 🛠️ Technologies Used

* Python 3.11
* Pygame

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
```

2. Create virtual environment:

```bash
python -m venv venv311
venv311\Scripts\activate
```

3. Install dependencies:

```bash
pip install pygame
```

---

## ▶️ Run the Game

```bash
python main.py
```

---

## 🎯 Controls

| Key | Action     |
| --- | ---------- |
| ↑   | Move Up    |
| ↓   | Move Down  |
| →   | Move Right |
| ←   | Move Left  |

---

## 🚀 Game Logic

* The snake moves in a grid system.
* When it eats food:

  * The snake grows
  * Speed increases (up to max = 12)
* If the snake hits itself:

  * Game ends
  * Automatically restarts after delay

---

## 🧠 Learning Goals

* Understanding game loops
* Handling user input
* Working with 2D grids
* Managing state (alive, direction, speed)
* Structuring Python projects

---

## 📌 Future Improvements

* Add score display
* Add sound effects
* Add pause feature
* Add levels/difficulty modes
* Improve graphics (filled blocks instead of borders)

---

## 👤 Author

Ali-RF92

---

## ⭐️ Support

If you like this project, consider giving it a ⭐ on GitHub!
