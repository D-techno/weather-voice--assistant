import requests
import pyttsx3
from plyer import notification
from datetime import datetime
import os
API_KEY = os.getenv("WEATHER_API_KEY")
CITY="Lucknow"
USERNAME="Dakshata"

def get_weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        main=data['main']
        weather=data['weather'][0]
        temp=main['temp']
        description=weather['description']
        description=description.title()
        return f"{description}. Temperature in the city is {temp} Kelvin"
    else:
        return f"Weather data not found . Try again later buddy !"
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def notifications(title,text):
    notification.notify(title=title,message=text,timeout=10,toast=True)
    print("Notification attempted.")


def greet_user():
    today=datetime.now().strftime("%A %B %d %Y")
    weather=get_weather(CITY)
    a=(f"Good morning {USERNAME}!!")
    b=(f"Today is {today}.\n")
    c=(f"Description of the weather in {CITY} is {weather}.\n Stay safe and have a great day ahead !!")
    greetings=a+b+c
    print(greetings)
    speak(greetings)
    notifications("WEATHER UPDATE",greetings)


greet_user()