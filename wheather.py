
import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt


api_key = "9d6e5c75f43a61a869bb71e4eb6b3913"


city_name = input("Please Enter Your City Name: ")


def time_from_utc_with_timezone(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

# Get the response from weather url
response = requests.get(weather_url)

# response will be in json format and we need to change it to pythonic format
weather_data = response.json()

# Make sure you get 200 as response to proceed
# SAMPLE DATA: {'coord': {'lon': 78.4744, 'lat': 17.3753}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 
# 'base': 'stations', 'main': {'temp': 293.04, 'feels_like': 293.44, 'temp_min': 291.15, 'temp_max': 294.82, 'pressure': 1015, 'humidity': 72}, 
# 'visibility': 6000, 'wind': {'speed': 1.58, 'deg': 163}, 'clouds': {'all': 0}, 'dt': 1614196800, 'sys': {'type': 1, 'id': 9213, 'country': 'IN', 
# 'sunrise': 1614215239, 'sunset': 1614257484}, 'timezone': 19800, 'id': 1269843, 'name': 'Hyderabad', 'cod': 200}

# weather_data['cod'] == '404' means city not found


if weather_data['cod'] == 200:
    kelvin = 273.15
    # Temperature shown here is in Kelvin and I will show in Celsius
    temp = int(weather_data['main']['temp'] - kelvin)
    feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed'] * 3.6
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']
    timezone = weather_data['timezone']
    cloudy = weather_data['clouds']['all']
    description = weather_data['weather'][0]['description']
    sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
    sunset_time = time_from_utc_with_timezone(sunset + timezone)

    print(f"Weather Information for City: {city_name}")
    print(f"Temperature (Celsius): {temp}")
    print(f"Feels like in (Celsius): {feels_like_temp}")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print("Wind speed: {0:.2f} km/hr".format(wind_speed))
    print(f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
    print(f"Cloud: {cloudy}%")
    print(f"Info: {description}")

    # Create a simple bar chart to visualize the weather data
    labels = ['Temperature', 'Feels Like', 'Pressure', 'Humidity', 'Wind Speed']
    values = [temp, feels_like_temp, pressure, humidity, wind_speed]
    plt.bar(labels, values)
    plt.xlabel('Weather Parameters')
    plt.ylabel('Values')
    plt.title('Weather Information')
    plt.show()

else:
    print(f"City Name: {city_name} was not found!")
