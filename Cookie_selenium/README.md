# Selenium Automation Suite

A Python automation project demonstrating advanced Selenium usage for web scraping, browser automation, form interaction, and game bots.

## Project Structure

SeleniumAutomation  
├── cookie.py # Full Cookie Clicker bot with automated upgrade purchasing  
├── main.py # Web scraper for extracting upcoming events from python.org  
├── interaction.py # Automated form submission and basic browser interactions  
└── README.md # This file  

## How to Use?

Install dependencies:
`pip install selenium`

Install ChromeDriver matching your Chrome version (or use ChromeDriver Manager).

Run script:
`main.py`

## Scripts Overview

### Cookie Clicker Bot — cookie.py
Automates the Cookie Clicker game with continuous clicking and smart upgrade purchasing.
* Clicks the cookie continuously
* Evaluates upgrade prices dynamically
* Purchases the most expensive affordable upgrade
* Runs for 5 minutes and prints Cookies-Per-Second (CPS)

### Python Scraper — main.py
Scrapes upcoming events from the official Python website and outputs a structured dictionary of {date: event_title}.
* Navigates to python.org
* Scrapes event titles and dates using CSS selectors
* Extracts attributes (get_attribute("datetime"))
* Aligns data into a clean dictionary

### Automated Form Submission — interaction.py
Automates form filling and submission on a test website.
* Fills in first name, last name, and email
* Submits the form automatically (Enter key)
* Maximizes window for better interaction

## Features
* Browser automation with Selenium
* Interaction with dynamic web pages
* CSS/XPath selectors
* Timed tasks and automated decision-making
* Practical examples: web scraping, form filling, game bot
* Clean and modular code for maintainability

## Technologies
* Python 3.12
* Selenium WebDriver (Chrome)
* Time for automation delays and scheduling
* CSS selectors & XPath
* Browser automation and element inspection

## Screenshots
<img width="1918" height="843" alt="image" src="https://github.com/user-attachments/assets/9cbe4789-61a3-4ced-8b95-527587e62143" />

