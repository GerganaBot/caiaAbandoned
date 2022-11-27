from django.shortcuts import render


def add_project(request):
    return render(request, template_name='projects/add-project-page.html')


def show_project_details(request):
    return render(request, template_name='projects/project-details.html')


def projects_list(request):
    return render(request, template_name='projects/project-list-page.html')
