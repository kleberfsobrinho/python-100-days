import requests
import smtplib
from twilio.rest import Client
from env import STOCK_API_KEY, NEWS_API_KAY, ACCOUNT_SID, AUTH_TOKEN, MY_EMAIL, MY_PASSWORD

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

PERCENT_REF = 2

params_query = {
    "function": "SYMBOL_SEARCH",
    "keywords": "apple",
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=params_query)
response.raise_for_status()

data = response.json()

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [
# new_value for (key, value) in dictionary.items()]

daily_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=daily_params)
response.raise_for_status()

data_daily = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data_daily.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "+"
else:
    up_down = "-"
difference = abs(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

diff_percent = difference / float(yesterday_closing_price) * 100

# Use the News API to get articles related to the COMPANY_NAME.
if diff_percent > PERCENT_REF:
    print("Sending message...")
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KAY
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()['articles']

    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation
    t_articles = articles[:3]
    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{round(diff_percent, 2)}%\nHeadline: {article['title']}.\n" \
                          f"Brief: {article['description']}\nLink: {article['url']}" for article in articles]
    msg = ""
    for s in formatted_articles:
        msg += s + "\n"

    # Send each article as a separate message via Twilio.
    # client = Client(ACCOUNT_SID, AUTH_TOKEN)
    # for article in formatted_articles:
    #     print(article)
    #     message = client.messages.create(
    #         body=article,
    #         from_='+14144046844',
    #         to='+5583981214614'
    #     )

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # security
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Stock Trading News Alert\n\n{msg}."
        )
