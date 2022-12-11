from django.db import models
from rest_framework.serializers import ModelSerializer

from caiaAbandoned.houses.models import House


class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
