from django.db import models

#simple value object model to store valuable information from api response
class WeatherVO(models.Model):
    dt = models.BigIntegerField(primary_key=True)
    dt_txt = models.DateTimeField()
    humidity = models.IntegerField()
    umbrella = models.BooleanField()