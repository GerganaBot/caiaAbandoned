from django.db import models
from rest_framework.serializers import ModelSerializer

from caiaAbandoned.houses.models import House, Location
from caiaAbandoned.projects.models import ProjectType, Project


class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
        read_only_fields = ("user",)


class ProjectTypeSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ("user",)

