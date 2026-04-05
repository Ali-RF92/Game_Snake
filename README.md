🐍 Snake Game — Python & Pygame

A classic Snake game built with Python and Pygame, developed as part of my hands-on learning in game development and real-time systems.

This project focuses on implementing core game mechanics, clean architecture, and responsive gameplay using a modular Python structure.

🎮 Gameplay Overview
Control the snake using arrow keys
Eat food to grow longer and increase speed
Avoid colliding with yourself
Game automatically restarts after death
✨ Key Features
Real-time keyboard input handling
Grid-based movement system
Dynamic speed scaling based on score
Self-collision detection
Automatic game restart with delay
Clean modular architecture (separation of concerns)
🧠 Technical Highlights
Structured game loop with clear state management
Separation of logic into dedicated modules
Frame-rate control (max 12 FPS) for consistent gameplay
Scalable design for adding features (levels, UI, effects)
🛠️ Tech Stack
Python 3.11
Pygame

⚙️ Setup & Installation
# Clone repository
git clone https://github.com/your-username/snake-game.git
cd snake-game

# Create virtual environment
python -m venv venv311
venv311\Scripts\activate

# Install dependencies
pip install pygame
▶️ Run the Game
python main.py
🎯 Controls
Key	Action
↑	Move Up
↓	Move Down
→	Move Right
←	Move Left
🚀 Game Mechanics
The snake moves on a fixed grid
Eating food:
Increases snake length
Increases speed (up to max 12 FPS)
Self-collision:
Ends the game
Triggers automatic restart after delay
📈 Future Improvements
Score display UI
Sound effects
Pause functionality
Difficulty levels
Enhanced graphics (filled tiles, animations)
👤 Author

Ali-RF92

⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.
