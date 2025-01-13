#checks the weather forcast for rain and sends sms via twilio if rain is expected
import requests
from twilio.rest import Client
#+12313039878

api_key="your_api_key"
endpoint="https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'your_acccount_sid'
auth_token = "your_authentication_token"


parameters={
    "lat":20.903000,
    "lon":85.174103,
    "appid":api_key,
    "cnt":4 #indicates 4 timestamp in a day
}
#fetch weather data using openweather api

responses=requests.get(endpoint,params=parameters)
responses.raise_for_status()
weather_data=responses.json()
#weather_id=weather_data["list"][0]["weather"][0]["id"]

will_rain=False
for hour in weather_data["list"]:
    condition_code=hour["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='twilio',
        body="It's going to rain today,Bring an umbrella",
        to='your_number'
    )
    print(message.status)