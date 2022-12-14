from django.db import models
from rest_framework.serializers import ModelSerializer

from caiaAbandoned.houses.models import House
from caiaAbandoned.projects.models import ProjectType


class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'house_location', 'house_photo', 'zone_name', 'street', 'street_number', 'description', 'square_meters',
                  'floors_number', 'construction_date', 'is_near_parking', 'is_near_park', 'is_near_metro', 'date_of_publication')


class ProjectTypeSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'
