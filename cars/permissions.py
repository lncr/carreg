from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model
from cars.models import Car


User = get_user_model()


class DiversePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        ru = request.user
        if request.method in SAFE_METHODS:
            return True
        elif ru.user_type == User.UserType.ADMIN:
            return True
        elif ru.user_type == User.UserType.PERSONAL_CABINET:
            if obj.status == Car.StatusType.REGISTRATION and ru == obj.owner:
                return True
        elif ru.user_type == User.UserType.SPECIALIST_1:
            if obj.status == Car.StatusType.LVL1 and ru == obj.worker:
                return True
        elif ru.user_type == User.UserType.SPECIALIST_2:
            if obj.status == Car.StatusType.LVL2 and ru == obj.worker:
                return True
        else:
            return False
