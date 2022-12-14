from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from caiaAbandoned.api.models import HouseSerializer, ProjectTypeSerializer
from caiaAbandoned.houses.models import House
from caiaAbandoned.projects.models import ProjectType


class ListHouseView(APIView):
    def get(self, request):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseDetail(APIView):
    def get_house(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        house = self.get_house(pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        house = self.get_house(pk)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        house = self.get_house(pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_project_types(request):
    project_types = ProjectType.objects.all()
    serializer = ProjectTypeSerializer(project_types, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_project_type(request):
    if request.user.is_authenticated:
        serializer = ProjectTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    raise PermissionDenied()


@api_view(['DELETE'])
def delete_project_type(self, request, pk):
    if request.user.is_authenticated:
        project_type = ProjectType(pk=pk)
        project_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
