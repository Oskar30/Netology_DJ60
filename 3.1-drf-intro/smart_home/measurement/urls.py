from django.urls import path
from measurement.views import SensorView, OneSensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensor/<pk>/', OneSensorView.as_view()),

]
