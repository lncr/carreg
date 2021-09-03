from rest_framework.viewsets import ModelViewSet

from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
