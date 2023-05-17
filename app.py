# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# API 엔드포인트 URL
url = '	http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
params = {
    'ServiceKey': os.getenv("WEATHER_SERVICE_KEY"),  # 사용자 인증키
    'numOfRows': '50',  # 한 페이지 결과 수
    'pageNo': '1',  # 페이지 번호
    'dataType': 'JSON',
    'base_date': '20230515',
    'base_time': '0600',
    'nx': '55',
    'ny': '127',
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

data = response.json()

print(json.dumps(data, indent=4, ensure_ascii=False))
