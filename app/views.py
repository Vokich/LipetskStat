from django.shortcuts import render, redirect
from .forms import AttractionForm, NewsForm
from .models import Attractions, News
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def page2_1(request):
    return render(request,'page2_sub1.html')

def page2_2(request):
    return render(request,'page2_sub2.html')

def page3_1(request):
    return render(request,'page3_sub1.html')

def page3_2(request):
    return render(request,'page3_sub2.html')

def map(request):
    return render(request,'map.html')


def news(request):
  if request.method == 'POST':
    form = NewsForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('news')
  else:
    form = NewsForm()
  try:
    news_items = News.objects.filter(is_published=True).order_by('-created_at')
  except:
    news_items = []
  return render(request, 'news.html', {
    'form': form,
    'news': news_items
  })
def attractions_view1(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST, request.FILES)
        if form.is_valid():
            attraction = form.save(commit=False)
            attraction.source = 'липецк'
            attraction.save()
            return redirect('attractions1')
    else:
        form = AttractionForm()

    attractions = Attractions.objects.filter(source='липецк')
    return render(request, 'page1_sub1.html', {'form': form, 'attractions': attractions})


def attractions_view2(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST, request.FILES)
        if form.is_valid():
            attraction = form.save(commit=False)
            attraction.source = 'елец'
            attraction.save()
            return redirect('attractions2')
    else:
        form = AttractionForm()

    attractions = Attractions.objects.filter(source='елец')
    return render(request, 'page1_sub2.html', {'form': form, 'attractions': attractions})

def get_weather(city):
    api_key = '02b8bf011c7481c1a7c702a1b7c1a8dc'  # Замените на ваш API ключ
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()


def get_forecast(city):
    api_key = '02b8bf011c7481c1a7c702a1b7c1a8dc'  # Замените на ваш API ключ
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()

def weather(request):
    weather_data = None
    forecast_data = None
    if request.method == 'POST':
        city = request.POST.get('city', 'Липецк')
        weather_data = get_weather(city)
        forecast_data = get_forecast(city)

    # Извлекаем влажность на завтра (индекс 1 в массиве forecast)
    humidity_tomorrow = None
    if forecast_data and len(forecast_data['list']) > 1:
        humidity_tomorrow = forecast_data['list'][1]['main']['humidity']

    return render(request, 'weather.html', {
        'weather_data': weather_data,
        'forecast_data': forecast_data,
        'humidity_tomorrow': humidity_tomorrow,
    })


