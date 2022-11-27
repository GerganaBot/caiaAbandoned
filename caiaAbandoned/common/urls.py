from django.urls import path, include
from caiaAbandoned.common import views
urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('aboutus/', views.about_us, name='about-us'),
    ]
