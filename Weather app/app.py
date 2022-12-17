import requests
from datetime import datetime

# API key to access data from website
api_key = '55806607ccd495170a39472519dbae18'
location = input("Enter City name: ")

# HTTP request to send and access data
weather_data = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'
)

# Error handling depending on the status code
if weather_data.json()['cod'] == '404':
    print("City not found!! Enter a valid city")
else:
    # gathering data from the json file and storing it in variables
    temp_city = weather_data.json()['main']['temp']
    weather_desc = weather_data.json()['weather'][0]['description']
    humidity = weather_data.json()['main']['humidity']
    wind_spd = weather_data.json()['wind']['speed']
    latitude = weather_data.json()['coord']['lat']
    longitude = weather_data.json()['coord']['lon']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    # displaying the data
    print("─────────────────────────────────────────────────────────────")
    print(f"Weather Stats for - {location} || {date_time}")
    print(f"Latitude  : {latitude}  \nLongitude : {longitude}")
    print("─────────────────────────────────────────────────────────────")

    print("Temperature          : {:.1f}°C".format(temp_city))
    print(f"Weather description  : {weather_desc}")
    print(f"Humidity             : {humidity}%")
    print(f"Wind speed           : {wind_spd}kmph")
