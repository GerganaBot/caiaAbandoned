from django.urls import path

from caiaAbandoned.api.models import LocationSerializer, ProjectTypeSerializer, ProjectSerializer
from caiaAbandoned.api import views
from caiaAbandoned.houses.models import Location
from caiaAbandoned.projects.models import ProjectType, Project

urlpatterns = [
    path('houses/', views.ListHouseView.as_view(), name='houses-all'),
    path('houses/<int:pk>/', views.HouseDetail.as_view(), name='house-detail'),
    path('project-types/', views.ListProjectTypesView.as_view(queryset=ProjectType.objects.all(), serializer_class=ProjectTypeSerializer), name='project-types-all'),
    path('project-types/<int:pk>/', views.ProjectTypesDetail.as_view(queryset=ProjectType.objects.all(), serializer_class=ProjectTypeSerializer), name='project-types-detail'),
    path('locations/', views.LocationsList.as_view(queryset=Location.objects.all(), serializer_class=LocationSerializer), name='locations-all'),
    path('locations/<int:pk>', views.LocationDetail.as_view(queryset=Location.objects.all(), serializer_class=LocationSerializer), name='locations-detail'),
    path('projects/', views.ProjectsList.as_view(queryset=Project.objects.all(), serializer_class=ProjectSerializer), name='projects-all'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(queryset=Project.objects.all(), serializer_class=ProjectSerializer), name='projects-detail'),
]
