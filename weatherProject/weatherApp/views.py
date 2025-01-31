from django.shortcuts import render
import urllib.request
import json

def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            try:
                source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=319aaa570f8d9b495315dda7e4097d42').read()
                list_of_data = json.loads(source)
                
                data = {
                    "country_code": list_of_data['sys']['country'],
                    "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                    "temp": f"{list_of_data['main']['temp']} °C",
                    "pressure": list_of_data['main']['pressure'],
                    "humidity": list_of_data['main']['humidity'],
                    "main": list_of_data['weather'][0]['main'],
                    "description": list_of_data['weather'][0]['description'],
                    "icon": list_of_data['weather'][0]['icon'],
                }
            except Exception as e:
                print(f"Error occurred: {e}")
    
    return render(request, "main/index.html", {"data": data})
