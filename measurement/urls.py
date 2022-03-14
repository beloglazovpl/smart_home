from django.urls import path

from measurement.views import SensorViewAll, UpdateSensor, AddMeasurement, MeasurementViewAll

urlpatterns = [
    path('sensors/', SensorViewAll.as_view()),
    path('sensors/<int:pk>/', UpdateSensor.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    path('measurements_all/', MeasurementViewAll.as_view())
]
