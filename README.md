# Weather API Application 🌦️

A backend Weather API application built using FastAPI and OpenWeather API integration.

## Features

- Get current weather by city
- Detailed weather report
- Query parameter support
- Unit selection (Celsius/Fahrenheit)
- Input validation
- Error handling
- Environment variable support
- Modular service architecture
- Automatic Swagger API documentation

## Technologies Used

- Python
- FastAPI
- Requests
- Pydantic
- OpenWeather API
- Uvicorn

## API Endpoints

### Home
GET /

### Health Check
GET /health

### Simple Weather
GET /weather/{city}

### Detailed Weather Report
GET /weather-report/{city}

### Search Weather with Query Params
GET /search-weather?city=chennai&unit=metric

## Project Structure

weather_api_app/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── models/
│   └── weather_model.py
│
├── services/
│   └── weather_service.py

## Concepts Practiced

- REST APIs
- API Integration
- JSON Parsing
- Query Parameters
- Path Parameters
- Response Models
- Environment Variables
- Modular Backend Architecture
- Validation & Error Handling

## Run Project

```bash
uvicorn main:app --reload
```

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```