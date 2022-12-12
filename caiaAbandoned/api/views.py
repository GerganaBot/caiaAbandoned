from django.core.exceptions import PermissionDenied

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
        return Response({'houses': serializer.data})


class RetrieveUpdateDestroyHouseAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()
    permission_classes = [IsAuthenticated]


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
            return Response(serializer.data)
    raise PermissionDenied()
