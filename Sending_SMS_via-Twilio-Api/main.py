import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your API key from openweathermap.org"
account_sid = "Your SID from Twilio"
auth_token = "Your TOKEN from Twilio"

weather_params = {
    "lat": 12345,
    "lon": 12345,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = (response.json())
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It;s going to rain today. Remember to bring an ☔",
        from_="Twilio Phone Number",
        to="To Sent Number",
    )
    print(message.sid)
    # print(message.status)
