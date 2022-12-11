from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('caiaAbandoned.api.urls')),
    path('', include('caiaAbandoned.common.urls')),
    path('accounts/', include('caiaAbandoned.accounts.urls')),
    path('houses/', include('caiaAbandoned.houses.urls')),
    path('projects/', include('caiaAbandoned.projects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
