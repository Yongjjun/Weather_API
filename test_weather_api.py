import pytest
import requests

# API URL 및 파라미터 설정
API_KEY = "2c5279c8fb164ae09bf112717250903"
url = "http://api.weatherapi.com/v1/current.json"

@pytest.mark.parametrize("city", ["Seoul", "New York", "Tokyo"])
# 날씨 API가 동작하는지 테스트
def test_weather_api(city):
    params = {"key": API_KEY, "q": city}
    response = requests.get(url, params=params)

    assert response.status_code == 200, f"API 요청 실패! 상태 코드: {response.status_code}"

    data = response.json()

    # 데이터 유효성 테스트
    assert "current" in data, "응답에 'current' 키 없음"
    assert "temp_c" in data["current"], "'temp_c' 키 없음"

    temp = data["current"]["temp_c"]

    # 기온 범위 체크 (-50도 ~ 50도)
    assert -50 <= temp <= 50, f"비정상적인 온도 값! {temp}°C"

    print(f"{city} 현재 온도: {temp}°C")

if __name__ == "__main__":
    pytest.main()