# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from .serializers import SensorSerializer

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


#@api_view(['GET', 'POST'])
#def demo(request):
#    if request.method == 'GET':
#        sensors = Sensor.objects.all()
#        ser = SensorSerializer(sensors, many=True)
#        #data = {'message':'hello'}
#        return Response(ser.data)
#
#    if request.method == 'POST':
#        return Response({'status':'ok'})


#class SensorView(APIView):
#    def get(self,request):
#        sensors = Sensor.objects.all()
#        ser = SensorSerializer(sensors, many=True)
#        return Response(ser.data)
#
#    def post(self,request):
#        return Response({'status':'ok'})


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


    def post(self,request):
        return Response({'status':'ok'})


class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
