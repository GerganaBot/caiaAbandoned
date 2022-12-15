from django.urls import path

from caiaAbandoned.api.models import LocationSerializer
from caiaAbandoned.api import views
from caiaAbandoned.houses.models import Location

urlpatterns = [
    path('houses/', views.ListHouseView.as_view(), name='houses-all'),
    path('houses/<int:pk>/', views.HouseDetail.as_view(), name='book-detail'),
    path('project-types/', views.ListProjectTypesView.as_view(), name='project-types-all'),
    path('project-types/<int:pk>/', views.ProjectTypesDetail.as_view(), name='project-types-detail'),
    path('locations/', views.LocationsList.as_view(queryset=Location.objects.all(), serializer_class=LocationSerializer), name='locations-all'),
    path('locations/<int:pk>', views.LocationDetail.as_view(queryset=Location.objects.all(), serializer_class=LocationSerializer), name='locations-all'),
]
