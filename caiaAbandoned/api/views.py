from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from caiaAbandoned.api.models import HouseSerializer
from caiaAbandoned.houses.models import House


class ListHouseView(APIView):
    def get(self, request):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response({'houses': serializer.data})

