import os 
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Extracts data from the OpenWeather API
def extract():
    city = 'berlin'
    units = 'metric'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f'Something went wrong the api request, the status code received was:{response.status_code}')

    return data

# Transform extracted raw data into a Pandas Dataframe 
def transform(data):
    
    return pd.DataFrame([{
        'city': data['name'],
        'country': data['sys']['country'],
        'time':datetime.fromtimestamp(data['dt']),
        'weather': data['weather'][0]['main'],
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'temperature_feel': data['main']['feels_like'],
        'humidity':data['main']['humidity']
    }])

# Loads the transformed data into a database in Postgresql server
def load(data_frame, table_name):
    DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    engine = create_engine(DATABASE_URL)

    data_frame.to_sql(table_name, engine, if_exists='append', index=False)


raw_data = extract()
weather_data_frame = transform(raw_data)
load(weather_data_frame,'berlin_weather')