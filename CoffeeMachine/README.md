# Coffee Machine

A Python console application simulating a Coffee Machine, demonstrating object-oriented programming concepts, control flow, and handling user input and resources.

## Project Structure

CoffeeMachine  
├── coffee_machine.py # Main program containing all functions  
└── README.md # This file  

## How to Use

1. Run the program:
  `python coffee_machine.py`
2. The machine will ask:
  *What would you like? (espresso/latte/cappuccino):*
Enter your choice.
3. 3. Commands:  
- `report` → Shows current resources (water, milk, coffee) and money earned  
- `off` → Turns off the machine
4. 4. If you choose a drink:  
- The program checks if enough resources are available  
- You will be prompted to insert coins:
  - Pennies ($0.01), Nickels ($0.05), Dimes ($0.10), Quarters ($0.25)  
- The machine calculates total inserted money, checks transaction, gives change if needed, updates resources, and serves your drink
5. Machine is starting to work from the beggining in infinite loop until `off` is typed.

## Features

- Simulates a working coffee machine with three types of drinks: espresso, latte, cappuccino  
- Resource management (water, milk, coffee)  
- Money handling with coin calculation and change returned  
- Handles insufficient resources and insufficient money  
- Modular functions for clean and readable code

## Technologies

- Python 3.12 
- Functions and control flow  
- Input handling and dealing with user's input 
- File handling (can be extended to save reports)

## Future Improvements

- Refactor code into classes for `CoffeeMachine`, `Drink`, `Resources`  
- Save money and resources state to a file .txt 
- Add more drink options and customizable sizes, more interaction with user 
- Add GUI interface with e.g. `Tkinter` 
  
