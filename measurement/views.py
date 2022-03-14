# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import ListCreateAPIView, get_object_or_404, \
    RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementAddSerializer, MeasurementSerializer


# Получить список Измерений
class MeasurementViewAll(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# получить список всех Сенсоров / создать новый Сенсор
class SensorViewAll(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def sensor_create(self, serializer):
        sensor = get_object_or_404(Sensor, name=self.request.data.get('name'),
                                   description=self.request.data.get('description'))
        return serializer.save(sensor=sensor)


# получить/обновить запись о Сенсоре по его ID
class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def sensor_update(self, serializer):
        sensor = get_object_or_404(Sensor, description=self.request.data.get('description'))
        return serializer.save(sensor=sensor)


# добавить Измерение для опредленного Сенсора
class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer
