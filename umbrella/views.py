from django.shortcuts import render
from datetime import datetime
from .models import WeatherVO

def home(request):
    #querying umrella days
    umbrellaDaysList = WeatherVO.objects.all().filter(umbrella=True)

    #new list to add umbrella days
    days = []

    #get current time to avoid past days from today
    today = datetime.now()

    #for each day in queried data list
    for day in umbrellaDaysList:
        #get weekday name
        weekday = day.when.strftime('%A')

        #set None TZ to avoid conflicts
        dt_day = day.when.replace(tzinfo=None)
        
        #check if day isnt already in list and if it is a future date
        if weekday not in days and dt_day > today:
            days.append(weekday)

    #set list in response, or none if empty
    response = days if len(days) > 0 else None
    
    return render(request, 'home.html', {'days' : response})
