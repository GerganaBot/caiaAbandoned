from django.urls import path, include
from caiaAbandoned.projects import views

urlpatterns = [
    path('addproject/', views.add_project, name='add-project-page'),
    path('projects/', views.projects_list, name='projects-list'),
    path('project/<slug:slug>/', include([
        path('', views.show_project_details, name='project-details'),
        path('myprojects/', views.my_projects, name='my-projects-page'),
    ]))
    ]
