from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from cars.models import Car
from cars.permissions import DiversePermission
from cars.serializers import CarSerializer
from accounts.tasks import send_mail_to_worker


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
<<<<<<< HEAD
    permission_classes = [IsAuthenticated & DiversePermission, ]
=======
    permission_classes = [IsAuthenticated, DiversePermission, ]

    @action(methods=['get', ], detail=True)
    def email_reminder(self, request, *args, **kwargs):
        car = self.get_object()
        if car.worker:
            send_mail_to_worker.delay()
            return Response('You have sent email to remind about this car')
        return Response('This car does not have worker associated with it', status=status.HTTP_404_NOT_FOUND)
>>>>>>> 6b34ce5bc9396cee3e5b86727c582d4afabf2e50
