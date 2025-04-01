import requests
from datetime import datetime


def get_coordinates(address):
    """Nominatim API를 사용해 주소의 좌표를 불러오기"""
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"

    headers = {
        "User-Agent": "MyWeatherApp/1.0 (myemail@example.com)"  # 자신을 식별할 수 있는 User-Agent
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data:
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            return lat, lon
        else:
            return None, None
    else:
        return None, None


def get_weather(lat, lon):
    """WeatherAPI를 사용해 위도, 경도로 날씨 정보 가져오기"""
    api_key = 'e579157aa5a04530b87235206253103'
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}&aqi=no"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]

        # 날씨 조건을 한글로 매핑
        condition_mapping = {
            "Clear": "맑음",
            "Partly cloudy": "구름 조금",
            "Cloudy": "흐림",
            "Overcast": "구름 많음",
            "Mist": "안개",
            "Patchy rain possible": "비 가능성 있음",
            "Patchy snow possible": "눈 가능성 있음",
            "Thundery outbreaks possible": "천둥 번개 가능성 있음",
            "Light rain": "가벼운 비",
            "Light snow": "가벼운 눈",
            "Heavy rain": "강한 비",
            "Heavy snow": "강한 눈",
            "Showers of rain": "비",
            "Showers of snow": "눈",
            "Rain": "비",
            "Snow": "눈",
            "Thunderstorm": "천둥번개",
            "Sunny" : "해가쨍쨍"
        }

        # 날씨 조건을 한글로 변환
        condition_korean = condition_mapping.get(condition, condition)  # 매핑되지 않으면 원래 상태 유지

        # 현재 시간을 가져와서 "현재 ~시"로 출력
        current_time = datetime.now().strftime("%H:%M")  # "HH:MM" 형태로 현재 시간 가져오기

        # 자연스러운 문장으로 날씨 출력
        return f"{condition_korean}입니다. (현재 {current_time} 기준)\n온도: {temp_c}°C"
    else:
        return "❌ 날씨 정보를 가져올 수 없습니다!"


def main():
    # 사용자로부터 주소 입력받기
    address = input("📍 주소를 입력하세요 (예: 사당동, 강남구, 서울시 서초구 등): ")

    # Nominatim API로 좌표 가져오기
    lat, lon = get_coordinates(address)

    if lat and lon:
        # WeatherAPI로 날씨 정보 가져오기
        weather_info = get_weather(lat, lon)
        # 사용자 입력을 그대로 반영해서 출력
        print(f"{address}의 날씨는 {weather_info}")
    else:
        print(f"❌ '{address}'에 대한 위치 정보를 찾을 수 없습니다.")


# 실행
main()
