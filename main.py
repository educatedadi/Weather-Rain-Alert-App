import requests
from twilio.rest import Client
import os

MY_API = os.environ.get("OWS_API")
MY_LAT = 51.507351  # Your Latitude
MY_LONG = -0.127758  # Your Longitude

twilio_sid = "AC8be37413d120bb67e05b025c41e8a578"
auth_token = os.environ.get("AUTH_TOKEN")

verified_mobile_number = os.environ.get("PHONE_NUM")

parameters = {
    "lat": deff_raining_lat,
    "lon": deff_raining_long,
    "appid": MY_API,
    "exclude": "current,minutely,daily",
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params=parameters
)

response.raise_for_status()
weather_data = response.json()

will_rain = False

hourly_data = weather_data["hourly"][:12]
for every_hour in hourly_data:
    if every_hour["weather"][0]['id'] < 700:
        will_rain = True
        break


if will_rain:
    client = Client(twilio_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today☔☔",
        to=verified_mobile_number,
        messaging_service_sid='MGce06d87f3acd11cc67484be81dca8182',
    )

    print(message.status)


