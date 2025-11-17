
import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_STOCK = "XXXXXXXXXXXX" # <-- this is personal
API_NEWS = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # <-- this is personal


MY_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "APP_PASSWORD"
TARGET_EMAIL = "destination_email@gmail.com"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": API_STOCK,
}

response1 = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response1.raise_for_status()
stock_data = response1.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
db_yesterday_data = stock_data_list[1]
db_yesterday_closing_price = db_yesterday_data["4. close"]

difference = abs(float(db_yesterday_closing_price) - float(db_yesterday_closing_price))
perc_difference = difference/float(db_yesterday_closing_price) * 100

if perc_difference > 5:
    news_params ={
        "apiKey": API_NEWS,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    ########

    message_body = "\n\n".join(formatted_articles)
    subject = f"Alert: TSLA zmiana {round(perc_difference, 2)}%!"

    email_message = f"Subject:{subject}\n\n{message_body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=email_message.encode("utf-8")
        )


