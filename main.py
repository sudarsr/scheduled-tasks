# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import requests
from twilio.rest import Client
import os
#twilio account details
api_key = os.environ.get("OWM_API_KEY")
sid = os.environ.get("ACCOUNT_SID")
token = os.environ.get("AUTH_TOKEN")

# https://api.openweathermap.org/data/4.0/onecall/current?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/4.0/onecall/timeline/1min?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/4.0/onecall/timeline/1day?lat={lat}&lon={lon}&appid={API key}
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
parameters={
    "lat":-27.469770,
    "lon":153.025,
    "appid":api_key,
     "cnt":4
}

url_weather='https://api.openweathermap.org/data/2.5/forecast'
response=requests.get(url=url_weather,params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data=response.json()

for i in range(0,3):
    if (weather_data["list"][i]['weather'][0]["id"])<700:
        print(type(weather_data["list"][i]['weather'][0]["id"]))
        print("carry an umbrella")
        client=Client(sid,token)
        # message = client.messages.create(
        #     from_="+12602548775", body="carry Umbrella", to="+61413960467"
        # )
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Bring an umbrella!!!',
            to='whatsapp:+61413960467')
    print(message.status)
