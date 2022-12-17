from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from caiaAbandoned.api.models import HouseSerializer, ProjectTypeSerializer, LocationSerializer, ProjectSerializer
from caiaAbandoned.houses.models import House, Location
from caiaAbandoned.projects.models import ProjectType, Project


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class HousesList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    project = House.objects.all()
    serializer_class = HouseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HouseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = House.objects.all()
    serializer_class = HouseSerializer

