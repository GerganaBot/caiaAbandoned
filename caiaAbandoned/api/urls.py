from django.urls import path, include

from caiaAbandoned.api.views import ListHouseView
from caiaAbandoned.common import views

urlpatterns = [
    path('houses/', ListHouseView.as_view(), name='houses-all'),
    ]
