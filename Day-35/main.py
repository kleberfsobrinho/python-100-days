import requests
from twilio.rest import Client
from env import API_KEY, ACCOUNT_SID, AUTH_TOKEN, CITY_LAT, CITY_LON

api_key = API_KEY

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

CG_LAT = CITY_LAT
CG_LON = CITY_LON

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": CG_LAT,
    "lon": CG_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

bring_umbrella = False
for hour in hourly_data:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂",
            from_='+14144046844',
            to='+5583981214614'
        )
