from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Car(models.Model):
    class StatusType(models.TextChoices):
        REGISTRATION = 'registration'
        LVL1 = 'lvl1'
        LVL2 = 'lvl2'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='handled_cars')
    mark = models.ForeignKey('directory.Mark', on_delete=models.PROTECT, related_name='cars')
    year_issue = models.IntegerField()
    legal_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=StatusType.choices, default=StatusType.REGISTRATION)

    def __str__(self):
        return self.legal_number


class CarDocument(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField()
