from django.urls import path
from measurement.views import CreateSensorAPIView, SensorUpdateView, MeasurementCreateView, SensorListAPIView, SensorRetrieveAPIView

urlpatterns = [
    path('sensors/create/', CreateSensorAPIView.as_view(), name='create-sensor'),
    path('sensors/<int:id>/update/', SensorUpdateView.as_view(), name='sensor-update'),
    path('measurements/<int:id>/create/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('sensors/list/', SensorListAPIView.as_view(), name='sensor-list'),
    path('sensors/<int:id>/', SensorRetrieveAPIView.as_view(), name='sensor-id'),
]