# Snake Game

A simple Snake game implemented in Python, demonstrating object-oriented programming, game logic, and basic file handling.

## Project Structure
SnakeGame  
├── main.py # Main game loop  
├── snake.py # Snake class, movement and growth  
├── food.py # Food class for generating food positions  
├── scoreboard.py # Scoreboard class for tracking and displaying score  
├── data.txt # File to save high score  
└── README.md # This file  

## How to Play?

1. Run `main.py` to start the game:
2. Control the snake using arrow keys:
- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **Left Arrow**: Move left
- **Right Arrow**: Move right
3. Eat the food to grow your snake and increase your score.
4. The game ends if the snake collides with the walls or itself (even his tail).
5. High score is saved in `data.txt` and displayed on the scoreboard.
6. The game restarts automatically and can be closed by Windows Button in the top-right corner.

## Features

- Object-oriented programming with separate classes for Snake, Food, and Scoreboard
- High score tracking using a simple text file (`data.txt`) (reading and writing to this file)
- Smooth game loop with real-time updates
- Simple and intuitive controls (by arrows)

- ## Technologies & Libraries

- Python 3.12
- `turtle` module for graphics
- `time` for little delay in game
- File handling for high score

- ## Screenshots

<img width="747" height="785" alt="image" src="https://github.com/user-attachments/assets/96215241-aa9f-4479-97ea-a2bc8b64c9ac" />

## Future Improvements

- Add levels or increasing speed
- Add sound effects or better image of the snake, background
- Implement GUI menu and restart options on request
