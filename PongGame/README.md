# Pong Game

A classic Pong game implemented in Python using the `turtle` module, demonstrating object-oriented programming, collision detection, and game loop management.

## Project Structure

PongGame  
├── main.py # Main game loop and event handling  
├── paddle.py # Paddle class for player-controlled paddles  
├── ball.py # Ball class with movement and bouncing logic  
├── scoreboard.py # Scoreboard class for tracking player scores  
└── README.md # This file  

## How to Play?

1. Run the program:
   `main.py`
2. Controls:  
- Right Paddle: **Up Arrow** (up), **Down Arrow** (down)  
- Left Paddle: **W** (up), **S** (down)  
3. Objective:  
- Keep the ball in play and try to make it pass the opponent's paddle to score points.
- Remember that ball cannot go out from the window by top or bottom  
4. Game ends when you close the window. Score is displayed on the top of the screen.

## Features

- Two-player Pong game simulation using the `turtle` graphics library  
- Object-oriented design with separate classes for `Ball`, `Paddle`, and `Scoreboard`  
- Smooth game loop with adjustable ball speed (depending on the score)  
- Collision detection with walls and paddles  
- Score tracking with real-time display

## Technologies & Concepts

- Python 3.12  
- Object-oriented programming (classes, methods, inheritance)  
- Game loop and timing (`time.sleep`)  
- Event handling with `screen.onkey()`  
- Basic 2D game physics (collision detection and response)

## Future Improvements

- Increase difficulty over time (higher ball speed, paddle size)
- Add start menu and restart option (more of GUI)
- Implement sound effects and visual enhancements

## Screenshots 

<img width="996" height="785" alt="image" src="https://github.com/user-attachments/assets/7ac06bac-3a62-431f-975f-e3e2cfec75fe" />
