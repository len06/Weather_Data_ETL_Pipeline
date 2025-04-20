import pandas as pd
from datetime import datetime

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
