from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c3f638ec0a394b157db681b02aeb07&units=metric'
    if(request.method =='POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()    
    cities = City.objects.all()
    weather_data=[]
    for city in cities:
        try:
            response = requests.get(url.format(city)).json()
            print(response)
            city_weather = {
                'city' : response['name'] ,
                'temperature' : response['main']['temp'],
                'description' : response['weather'][0]['description'],
                'icon' : response['weather'][0]['icon'],
            }
            weather_data.insert(0,city_weather)
        except Exception:
            continue
    context = {'weather_data' : weather_data,'form':form,}
    return render(request,'weather/weather.html', context)
# proceed with city
