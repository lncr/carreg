from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=128)


class Mark(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='marks')
    name = models.CharField(max_length=128)
