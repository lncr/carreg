from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from cars.models import Car
from cars.permissions import DiversePermission
from cars.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, DiversePermission, ]
