from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework.views import APIView

from caiaAbandoned.api.models import HouseSerializer, ProjectTypeSerializer, LocationSerializer
from caiaAbandoned.houses.models import House, Location
from caiaAbandoned.projects.models import ProjectType


class ListHouseView(APIView):
    def get(self, request):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseDetail(APIView):
    def get_house(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        house = self.get_house(pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def put(self, request, pk):
        house = self.get_house(pk)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        house = self.get_house(pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListProjectTypesView(APIView):
    def get(self, request):
        houses = ProjectType.objects.all()
        serializer = ProjectTypeSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectTypesDetail(APIView):
    def get_project_type(self, pk):
        try:
            return ProjectType.objects.get(pk=pk)
        except ProjectType.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project_type = self.get_project_type(pk)
        serializer = ProjectTypeSerializer(project_type)
        return Response(serializer.data)

    def put(self, request, pk):
        project_type = self.get_project_type(pk)
        serializer = ProjectTypeSerializer(project_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project_type = self.get_project_type(pk)
        project_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationsList(ListCreateAPIView):
    location = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
