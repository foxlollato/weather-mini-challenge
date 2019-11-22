from django.shortcuts import render
from datetime import datetime
from .models import WeatherVO

def home(request):
    #get current time to avoid past days from today
    today = datetime.now()

    #querying umbrella filtered by forward days 
    umbrellaDaysList = WeatherVO.objects.all().filter(umbrella=True, dt_txt__gt=today)

    #getting list to add umbrella weekdays once each
    days = list(dict.fromkeys([day.dt_txt.strftime('%A') for day in umbrellaDaysList]))

    #set list in response, or none if empty
    response = days if len(days) > 0 else None
    
    return render(request, 'home.html', {'days' : response})
