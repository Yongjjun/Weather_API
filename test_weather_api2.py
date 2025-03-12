import json
import pytest
import requests
import logging
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# API URL 및 파라미터 설정
API_KEY = os.getenv("API_KEY") # .env 또는 GitHub Secrets에서 API_KEY 가져오기
# API URL 설정
url = "http://api.weatherapi.com/v1/current.json"

# 로그 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.mark.parametrize("city", ["Seoul", "New York", "Tokyo"])
def test_weather_api(city):
    params = {"key": API_KEY, "q": city}
    response = requests.get(url, params=params)

    assert response.status_code == 200, f"API 요청 실패! 상태 코드: {response.status_code}"
    data = response.json()

    assert "current" in data, "응답에 'current' 키 없음"
    assert "temp_c" in data["current"], "'temp_c' 키 없음"

    temp = data["current"]["temp_c"]
    assert -50 <= temp <= 50, f"비정상적인 온도 값! {temp}°C"

    # print(f"{city} 현재 온도: {temp}°C")

    weather_info = {
        "city": city,
        "temperature": temp,
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"]
    }

    logging.info(f"{city} 현재 온도: {temp}°C, 상태: {weather_info['condition']}, 습도: {weather_info['humidity']}%")

    # JSON 데이터 저장 (기존 데이터 유지)
    try:
        with open('weather_result.json', 'r', encoding='utf-8') as f:
            all_weather_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_weather_data = []

    all_weather_data.append(weather_info)

    with open('weather_result.json', 'w', encoding='utf-8') as f:
        json.dump(all_weather_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pytest.main()
