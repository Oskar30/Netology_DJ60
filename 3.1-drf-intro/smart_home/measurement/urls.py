from django.urls import path
from measurement.views import SensorView, SensorDetail, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
