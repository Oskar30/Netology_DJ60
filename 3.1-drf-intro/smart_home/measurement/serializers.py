from rest_framework import serializers
from .models import Sensor


#class SensorSerializer(serializers.Serializer):
#    #id = serializers.IntegerField()
#    name = serializers.CharField()


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name']