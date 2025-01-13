#Easy Level
from http.client import responses
from twilio.rest import Client
import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="stock api"
NEWS_API_KEY="news_api_key"
TWILIO_SID="twilio_sid"
TWILIO_AUTH_TOKEN="twilio_auth_key"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response=requests.get(STOCK_ENDPOINT,params=stock_parameters)
#print(response.json())
data=response.json()["Time Series (Daily)"]
data_list=[value for(key,value) in data.items()]
yesturday_data=data_list[0]
yesturday_closing_price=yesturday_data["4. close"]
print(yesturday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesturday=data_list[1]
day_before_yesturday_closing_price=day_before_yesturday["4. close"]
print(day_before_yesturday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=abs(float(yesturday_closing_price)-float(day_before_yesturday_closing_price))
print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference=(difference/float(yesturday_closing_price))*100
print(percentage_difference)



## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#If percentage is greater than 5 then print("Get News").
if percentage_difference<1:
    news_parameters={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,

    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_parameters)
    articles=news_response.json()["articles"]
    print(articles)

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles=articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles=[f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#TODO 9-end each article as a separate message via Twilio.
    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message=client.messages.create(
            body=article,
            from_="+12313039878",
            to="+919901066494"
        )

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
