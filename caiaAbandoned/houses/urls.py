from django.urls import path, include
from caiaAbandoned.houses import views

urlpatterns = [
    path('addhouse/', views.add_house, name='house-add'),
    path('houseslist/', views.houses_list, name='houses-list'),
    path('house/<slug:slug>/', include([
        path('housedetails', views.show_house_details, name='house-details'),
        path('myhouses/', views.my_houses, name='my-houses-page'),
        path('edit/', views.edit_house, name='edit-house-page'),
        path('delete/', views.delete_house, name='delete-house-page'),
    ]))
    ]
