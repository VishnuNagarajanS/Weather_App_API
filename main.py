from fastapi import FastAPI,Query
from services.weather_service import fetch_weather,fetch_detailed_weather
from models.weather_model import WeatherResponse,DetailedWeatherResponse
app=FastAPI()
@app.get("/")
def home():
    return {
        "message":"Weather API App Running"
    }
@app.get("/weather/{city}", response_model=WeatherResponse)
def get_weather(city: str):
    return fetch_weather(city)
@app.get("/weather-report/{city}",response_model=DetailedWeatherResponse)
def weather_report(city:str):
    return fetch_detailed_weather(city)
@app.get("/search-weather")
def search_weather(city: str = Query(...,min_length=2,max_length=30,description="Enter city name"),unit:str=Query("metric",description="metric or imperial")):    
    return fetch_weather(city,unit)
@app.get("/health")
def health_check():
    return {
        "status": "API is running successfully"
    }
