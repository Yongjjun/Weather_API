# Weather_API

# 사용 기술
- Python
- Pytest
- Requests
- JSON 파일 저장

# 설치 및 실행 방법
## 1. 환경 설정
pip install pytest requests

## 2. 환경 변수 설정 (API Key 관리)
API 키는 코드에 직접 포함하지 않고 .env 파일 또는 환경 변수로 관리하는 것이 좋습니다.
.env 파일 예시 : 
API_KEY=your_api_key_here

## 3. 테스트 실행
pytest weather_test.py

# 테스트 설명
## 1. API 응답 테스트
- 서울, 뉴욕, 도쿄 3개의 도시를 대상으로 API 응답을 테스트합니다.
- HTTP 응답 코드가 200인지 확인합니다.
- 응답 데이터에 current.temp_c 필드가 포함되어 있는지 검증합니다.
- 기온 값이 -50°C ~ 50°C 범위 내에 있는지 확인합니다.

## 2. 테스트 데이터저장
- 테스트를 실행하면 각 도시의 날씨 정보가 weather_result.json 파일에 저장됩니다.
- 저장되는 데이터 예시 :
[
  {
    "city": "Seoul",
    "temperature": 12.3,
    "condition": "Clear",
    "humidity": 56
  }
]

## 추가개선 사항
- API 키를 .env 파일에서 로드하도록 수정
- logging 모듈을 사용하여 테스트 결과 로깅
- 테스트 실행 시 기존 JSON 데이터를 유지하는 방식 개선
