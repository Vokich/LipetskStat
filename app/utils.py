#import requests
#from django.conf import settings
#from .models import WeatherCache
#
#
#def get_weather_data():
#    params = {
#        'lat': settings.LIPETSK_COORDS['lat'],
#        'lon': settings.LIPETSK_COORDS['lon'],
#        'appid': settings.OPENWEATHERMAP_API_KEY,
#        'units': 'metric',  # Для получения температуры в °C
#        'lang': 'ru'
#    }
#
#    try:
#        response = requests.get(settings.OPENWEATHERMAP_API_URL, params=params)
#        response.raise_for_status()
#        data = response.json()
#
#        # Сохраняем данные в кэш
#        WeatherCache.objects.create(
#            temperature=data['main']['temp'],
#            description=data['weather'][0]['description'],
#            humidity=data['main']['humidity'],
#            wind_speed=data['wind']['speed']
#        )
#
#        return {
#            'temperature': data['main']['temp'],
#            'description': data['weather'][0]['description'],
#            'humidity': data['main']['humidity'],
#            'wind_speed': data['wind']['speed']
#        }
#    except Exception as e:
#        # Если API не работает, возвращаем последние сохраненные данные
#        last_cache = WeatherCache.objects.last()
#        if last_cache:
#            return {
#                'temperature': last_cache.temperature,
#                'description': last_cache.description,
#                'humidity': last_cache.humidity,
#                'wind_speed': last_cache.wind_speed
#            }
#        return None