import requests
from fastapi import HTTPException
import os
from dotenv import load_dotenv

def fetch_weather(city: str, unit: str):
    api_key = os.getenv("API_KEY")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units={unit}"
    )
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )
    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }
    return weather_data
def fetch_detailed_weather(city:str):
    api_key=os.getenv("API_KEY")
    url=(f"https://api.openweathermap.org/data/2.5/weather"
         f"?q={city}&appid={api_key}&units=metric")
    response=requests.get(url)
    data=response.json()
    if response.status_code!=200:
        raise HTTPException(
            status_code=404,
            detail="city not found"
        )
    detailed_weather={
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "feels_like": data["main"]["feels_like"],
        "wind_speed": data["wind"]["speed"],
        "country": data["sys"]["country"]
    }
    return detailed_weather

load_dotenv()