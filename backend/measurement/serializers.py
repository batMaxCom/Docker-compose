from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializers(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']
