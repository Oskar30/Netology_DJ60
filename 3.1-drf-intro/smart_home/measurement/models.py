from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):    
    name = models.CharField(max_length=30)


class Measurement(models.Model):
    # id
    temp = models.FloatField
    time = models.DateTimeField
