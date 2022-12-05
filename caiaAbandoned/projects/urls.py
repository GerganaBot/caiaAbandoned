from django.urls import path, include
from caiaAbandoned.projects import views

urlpatterns = [
    path('addproject/', views.add_project, name='add-project-page'),
    path('projects/', views.projects_list, name='projects-list'),
    path('project/<slug:slug>/', include([
        path('projectdetails', views.show_project_details, name='project-details'),
        path('myprojects/', views.my_projects, name='my-projects-page'),
        path('edit/', views.edit_project, name='edit-project-page'),
        path('delete/', views.delete_project, name='delete-project-page'),
    ]))
    ]
