import requests

def get_coordinates():
    """Nominatim API를 사용해 사당동의 좌표를 불러오기"""
    address = "사당동, 대한민국"
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
            full_address = data[0]["display_name"]
            print(f"입력한 주소: {address}")
            print(f"검색된 주소: {full_address}")
            print(f"위도: {lat}, 경도: {lon}")
        else:
            print(f"❌ '{address}'에 대한 위치 정보를 찾을 수 없습니다.")
    else:
        print("❌ Nominatim API 요청 실패!")

# 실행
get_coordinates()
