from django.urls import path, include
from caiaAbandoned.api.views import ListHouseView, HouseDetail
from caiaAbandoned.api import views

urlpatterns = [
    path('houses/', ListHouseView.as_view(), name='houses-all'),
    path('houses/<int:pk>/', HouseDetail.as_view(), name='book-detail'),
    path('project-types/', views.get_project_types, name='project-types-all'),
    path('project-types/<int:pk>', views.delete_project_type, name='project-type-delete'),
    path('project-types/add/', views.post_project_type, name='create-project-type')

]
