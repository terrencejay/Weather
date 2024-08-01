from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):

    # request_url = f'https://api.tomorrow.io/v4/weather/realtime?appid={os.getenv("API_KEY")}&location={city}&units=imperial'
    # headers = {"accept": "application/json"}
    # response = requests.get(request_url, headers=headers)
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(response.text)

    # request_url = f'http://api.openweathermap.org/data/3.0/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    if not bool(city.strip()):
        city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")

    pprint(weather_data)