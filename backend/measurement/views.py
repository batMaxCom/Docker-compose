# TODO: опишите необходимые обработчики,
#  рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, \
    CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializers, \
    MeasurementSerializers, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.order_by('id')
    serializer_class = SensorSerializers


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk=None):
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializers(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializers

    def post(self, request):
        data = request.data
        measurements = Measurement(
            sensor_id=data.get('sensor'),
            temperature=data.get('temperature'),
            image=data.get('image')
        )
        measurements.save()
        return Response(data)
