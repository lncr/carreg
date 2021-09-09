from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'owner', 'worker', 'mark', 'year_issue', 'legal_number', 'status', ]
        read_only_fields = ['owner', ]
