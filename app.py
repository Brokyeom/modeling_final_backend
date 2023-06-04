from flask import Flask, request, jsonify
from flask_cors import CORS

import openai
import os
import geocoder
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
API_KEY = os.getenv("WEATHER_SERVICE_KEY")

@app.route('/', methods=['GET'])
def get_location():
    try:
        g = geocoder.ip('me')
        return get_weather(g.lat, g.lng)
    except Exception as e:
        print("Can't find you. No weather for you.")

get_location()

def get_weather(lat, long):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    city = data['name']
    weather = data['weather'][0]['main']
    temp = data['main']['temp']

    return f'{city}의 날씨는 {weather}, 기온은 {temp}도 입니다.'

@app.route('/input', methods=['POST'])
def get_input():
    data = request.get_json()

    if 'inputValue' not in data:
        return jsonify({'message': 'No input value provided'}), 400

    input_text = data['inputValue']
    
    return jsonify({'message': f'Received input: {input_text}'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
