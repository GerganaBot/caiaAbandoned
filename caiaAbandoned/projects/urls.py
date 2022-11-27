from django.urls import path, include
from caiaAbandoned.projects import views

urlpatterns = [
    path('addproject/', views.add_project, name='project-add'),
    path('projects/', views.projects_list, name='projects-list'),
    path('project/<int:pk>/', include([
        path('', views.show_project_details, name='project-details'),
    ]))
    ]
