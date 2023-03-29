from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from measurement.serializers import SensorSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement


class CreateSensorAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save()


class SensorUpdateView(UpdateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
    lookup_url_kwarg = 'id'

    def perform_update(self, serializer):
        serializer.save()


class MeasurementCreateView(CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        serializer.save()


class SensorListAPIView(ListAPIView):
    queryset = Sensor.objects.all().values('id', 'name', 'description')
    serializer_class = SensorSerializer


class SensorRetrieveAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'id'
