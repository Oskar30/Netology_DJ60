from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):    
    # id
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return f'{self.name} {self.description}'


class Measurement(models.Model):
    # id
    temperature = models.FloatField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SensorReadings(models.Model):
    #id
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='Readings')
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)