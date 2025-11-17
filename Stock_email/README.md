A Python automation script that monitors daily stock price changes for Tesla (TSLA).  
If the price movement exceeds a specified threshold, the script fetches the latest related news and sends an email alert.

This project demonstrates API integration, data processing, automation, error handling, and email notifications.

## Project Structure

StockAlert  
├── main.py # Main script handling stock data, news retrieval, and email notifications  
└── README.md # This file  

## How It Works?

1. Fetches daily stock price data from **Alpha Vantage API**.
2. Calculates the difference between yesterday's closing price and the previous day's closing price.
3. If the percentage change exceeds **5%**, the script:
   - Queries **NewsAPI** for the latest articles related to Tesla.
   - Extracts the top 3 headlines and summaries.
   - Sends an email alert containing:
     - % change  
     - Headlines  
     - Short descriptions

## APIs Used

### 🔹 Alpha Vantage  
Used for retrieving daily TSLA stock prices.  
Endpoint: `https://www.alphavantage.co/query`

### 🔹 NewsAPI  
Used for fetching the latest news about Tesla.  
Endpoint: `https://newsapi.org/v2/everything`

## Requirements

Install required packages:
`pip install requests`

If sending emails with Gmail, you must create an **App Password** and enable 2FA.


## Configuration

In `main.py`, set up your info:

MY_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TARGET_EMAIL = "recipient@gmail.com"
API_STOCK = "YOUR_ALPHA_VANTAGE_KEY"
API_NEWS = "YOUR_NEWSAPI_KEY"

## How to Run?
Run : `python main.py`
The script runs once and sends an email alert if the condition is met.

To automate it daily, run it using:
* Windows Task Scheduler
* Cloud automation tools (AWS Lambda, PythonAnywhere, etc.)

## Features

* Automated stock price monitoring
* Daily price difference calculation
* Fetching relevant news articles
* Email alert system with formatted content
* Clean, modular, easy-to-read code
* Example of a real-world Python automation workflow

## Future Improvements

* Improve calculation logic (fix difference bug)
* Add support for multiple stocks
* Add SMS alerts using Twilio
* Save logs to a file
* Deploy as a scheduled cloud function
* Build a simple dashboard

## Notes

⚠️ This project uses API keys.
Never commit real keys or passwords to GitHub.
Use environment variables or a .env file (e.g. with python-dotenv) in production.



