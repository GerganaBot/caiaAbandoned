from django.shortcuts import render

from caiaAbandoned.projects.models import Project


def show_project_details(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        'project': project,
    }
    return render(request, template_name='projects/project-details.html', context=context)


def projects_list(request):
    all_projects = Project.objects.all()
    context = {
        'all_projects': all_projects
    }
    return render(request, template_name='projects/project-list-page.html', context=context)


def add_project(request):
    return render(request, template_name='projects/add-project-page.html')


def my_projects(request):
    return render(request, template_name='projects/my-projects-page.html')

