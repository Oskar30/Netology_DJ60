from django.contrib import admin

from .models import Sensor, Measurement



@admin.register(Sensor)
class ArticleAdmin(admin.ModelAdmin):
    pass
   


@admin.register(Measurement)
class TagAdmin(admin.ModelAdmin):
    pass