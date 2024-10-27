import requests

import setting
from .route import route


# Роутинг для событий
@route.post("/uv")
def create_event():
    access_key = setting.YASHA_POGODA_KEY

    headers = {'X-Yandex-Weather-Key': access_key}
    response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=47.222110&lon=39.718808',
                            headers=headers).json()
    return response['fact']['uv_index']
