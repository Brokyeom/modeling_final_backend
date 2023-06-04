from flask import Flask, request
import openai
import os
import geocoder
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_SERVICE_KEY")

@app.route('/', methods=['GET'])
def get_weather(lat, long):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']

    return temp

def get_location():
    try:
        g = geocoder.ip('me')
        return g.lat, g.lng
    except Exception as e:
        print("Can't find you. No weather for you.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
