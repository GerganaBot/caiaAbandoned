from django.urls import path, include
from caiaAbandoned.api.views import ListHouseView, RetrieveUpdateDestroyHouseAPIView
from caiaAbandoned.api import views

urlpatterns = [
    path('houses/', ListHouseView.as_view(), name='houses-all'),
    path('houses/<int:pk>/', RetrieveUpdateDestroyHouseAPIView.as_view(), name='book-detail'),
    path('project-types/', views.get_project_types, name='project-types-all'),
    path('project-types/add/', views.post_project_type, name='create-project-type')

]
