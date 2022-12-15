from django.http import Http404
from rest_framework import status

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView

from caiaAbandoned.api.models import HouseSerializer, ProjectTypeSerializer, LocationSerializer, ProjectSerializer
from caiaAbandoned.houses.models import House, Location
from caiaAbandoned.projects.models import ProjectType, Project


# class ListHouseView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get(self, request):
#         houses = House.objects.all()
#         serializer = HouseSerializer(houses, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = HouseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class HouseDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_house(self, pk):
#         try:
#             return House.objects.get(pk=pk)
#         except House.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         house = self.get_house(pk)
#         serializer = HouseSerializer(house)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         house = self.get_house(pk)
#         serializer = HouseSerializer(house, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         house = self.get_house(pk)
#         house.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ListProjectTypesView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    project_type = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class ProjectTypesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class LocationsList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    location = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ProjectsList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    project = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class HousesList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    project = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = House.objects.all()
    serializer_class = HouseSerializer

