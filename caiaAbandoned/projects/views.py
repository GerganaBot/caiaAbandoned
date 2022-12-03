from django.shortcuts import render


def show_project_details(request):
    return render(request, template_name='projects/project-details.html')


def projects_list(request):
    return render(request, template_name='projects/project-list-page.html')
