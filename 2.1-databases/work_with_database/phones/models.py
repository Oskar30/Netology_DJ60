from django.db import models


class Phone(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.CharField(max_length=50, default=None)
