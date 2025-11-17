# Turtle Crossing Game

A Python arcade-style game inspired by the classic Frogger. The goal is to help the turtle cross the road while avoiding moving cars. This project demonstrates object-oriented programming, collision detection, dynamic difficulty scaling, and event-driven gameplay using the `turtle` module.

## Project Structure

TurtleCrossing  
├── main.py # Main game loop and event handling  
├── player.py # Player class controlling the turtle  
├── car_manager.py # CarManager class for generating and moving cars  
├── scoreboard.py # Scoreboard class for levels and game over display  
└── README.md # This file  

## How to Play?

1. Run the game:
   `main.py`
2. Controls:  
- **Up Arrow** → Move the turtle forward

3. Objective:  
- Dodge the cars and reach the finish line at the top of the screen.
- Each time you cross successfully, the level increases and cars move faster.

4. The game ends when the turtle collides with a car.

## Features

- OOP architecture with clean separation of responsibilities  
- Randomized car generation with varied colors and positions (rectangles)  
- Increasing difficulty with each level (cars accelerate)  
- Collision detection between the player and cars  
- Score tracking and clear game-over message  
- Smooth animation using `screen.tracer()` and timed updates

## Technologies

- Python 3.12
- `turtle` module for simple graphics and `screen` for screen setup 
- Object-oriented programming (classes, inheritance)  
- Game loop and timing (`time.sleep`)  
- Event-driven input handling  
- Randomization and dynamic difficulty

## Future Improvements

- Add left/right movement for the player  
- Add sound effects and improved animations  
- Implement pause/menu screens  
- Add “lives” system instead of instant game over (better GUI)  
- Change image of cars from basic rectangles

## Screenshots

<img width="747" height="784" alt="image" src="https://github.com/user-attachments/assets/23b4ce73-9fda-4e15-9852-1a80ba2233f6" />
