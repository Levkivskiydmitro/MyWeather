import requests

api_key = 'ac90bee491d306ada1c92f65cd9f3482'
first_city_name = 'Днепр'
lang = 'ua'

url = f'https://api.openweathermap.org/data/2.5/forecast?q={first_city_name}&appid={api_key}&lang={lang}'

responce = requests.get(url)

if responce.status_code == 200:
    data = responce.json()

    hourly_weather = round(data['list'][0]['main']['temp'] - 273.15)
    hourly_weather = str(hourly_weather)
    hourly_weather = 'В следующем часу: '+ hourly_weather + " Градусов"
    # hourly_temperature = data['list'][0]['main']['weather']['temp']

    
    print(hourly_weather)