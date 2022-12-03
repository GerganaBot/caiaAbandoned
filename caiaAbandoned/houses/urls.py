from django.urls import path, include
from caiaAbandoned.houses import views

urlpatterns = [
    path('addhouse/', views.add_house, name='house-add'),
    path('houseslist/', views.houses_list, name='houses-list'),
    path('housedetails<slug:slug>', views.show_house_details, name='house-details'),
    ]
