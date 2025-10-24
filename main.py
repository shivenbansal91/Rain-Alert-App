import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_API_KEY"

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

weather_params = {
    "lat": "YOUR_LOCATION_LAT" ,
    "lon": "YOUR_LOCATION_LONG",
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWM_endpoint,params= weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hourly_data in  weather_data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if(int(condition_code) < 700):
       will_rain = True

if(will_rain):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body="It's going to be rain today. Remember to bring an ☂️.",
    from_= "+1xxxxxxxxxx",
    to= "+91xxxxxxxxxx",
)
    print(message.status)
