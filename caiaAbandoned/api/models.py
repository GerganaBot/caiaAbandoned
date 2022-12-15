from django.db import models
from rest_framework.serializers import ModelSerializer

from caiaAbandoned.houses.models import House
from caiaAbandoned.projects.models import ProjectType


class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class ProjectTypeSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'
