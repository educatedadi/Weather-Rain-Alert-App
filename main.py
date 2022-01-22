import requests
from twilio.rest import Client

my_email = "adisenpai101@gmail.com"
password = "ar_@12345"

MY_API = "43714508be1015dd968c7fbbc552f7b1"
MY_LAT = 24.047930  # My Latitude
MY_LONG = 84.069099  # My Longitude

twilio_sid = "AC8be37413d120bb67e05b025c41e8a578"
auth_token = "a8f23380f3e0a4712f93e7babc5d9943"

deff_raining_lat = -18.157132
deff_raining_long = 49.409860

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
        to='+919135620787',
        messaging_service_sid='MGce06d87f3acd11cc67484be81dca8182',
    )

    print(message.status)


