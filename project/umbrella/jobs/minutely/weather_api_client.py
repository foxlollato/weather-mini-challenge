from django_extensions.management.jobs import MinutelyJob
import requests
from datetime import datetime
from  umbrella.models import WeatherVO
from django.conf import settings

apiString = settings.WEATHER_API_STRING #API STRING from settings.py

#weather api client job created to be exec on schedule and avoid direct access to openweather api
class Job(MinutelyJob):
    help = "Consume weather api"

    def execute(self):
        #get api response
        response = requests.get(apiString)

        #json format
        weatherdata = response.json()        
        
        #filtering valuable information from response
        for weather in weatherdata['list']:
            #store id
            dt = int(weather['dt'])
            
            #weather date
            when = datetime.strptime(weather['dt_txt'], '%Y-%m-%d %H:%M:%S')
            
            #humidity
            humidity = weather['main']['humidity']
            
            #and if this day should take umbrella
            umbrella = True if humidity > 70 else False
            
            #creating and storing object
            vo = WeatherVO(dt, when, humidity, umbrella)
            vo.save()
