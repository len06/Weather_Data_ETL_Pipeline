import os
import requests

def extract(city='Berlin'):
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    
    units = 'metric'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={API_KEY}'

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Something went wrong when obtaining the data: {response.status_code}')
