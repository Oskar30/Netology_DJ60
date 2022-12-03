from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
