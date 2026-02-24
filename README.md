# Weather Voice Assistant 🌦️

This Python project fetches real-time weather data using OpenWeather API, speaks the weather update using text-to-speech, and shows a desktop notification.

## Features
- Fetches live weather data
- Converts weather description into speech
- Shows system notification
- Personalized greeting

## Technologies Used
- Python
- Requests
- pyttsx3
- Plyer
- OpenWeather API

## How to Run
1. Install requirements:
   pip install -r requirements.txt
2. Set environment variable:
   setx WEATHER_API_KEY "your_api_key"
3. Run:
   python weather_api.py