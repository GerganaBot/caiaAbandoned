from django.urls import path
from caiaAbandoned.api.views import ListHouseView, HouseDetail, ProjectTypesDetail
from caiaAbandoned.api import views

urlpatterns = [
    path('houses/', ListHouseView.as_view(), name='houses-all'),
    path('houses/<int:pk>/', HouseDetail.as_view(), name='book-detail'),
    path('project-types/', views.ListProjectTypesView.as_view(), name='project-types-all'),
    path('project-types/<int:pk>/', ProjectTypesDetail.as_view(), name='project-types-detail'),
]
