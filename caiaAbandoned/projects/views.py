from django.shortcuts import render


def show_project_details(request):
    return render(request, template_name='projects/project-details.html')


def projects_list(request):
    return render(request, template_name='projects/project-list-page.html')


def add_project(request):
    return render(request, template_name='projects/add-project-page.html')


def my_projects(request):
    return render(request, template_name='projects/my-projects-page.html')

