from pydantic import BaseModel


class WeatherResponse(BaseModel):

    city: str
    temperature: float
    humidity: int
    weather: str
class DetailedWeatherResponse(BaseModel):
    city: str
    temperature: float
    humidity: int
    weather: str
    feels_like: float
    wind_speed: float
    country: str

    