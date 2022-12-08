from django.shortcuts import render, redirect

from caiaAbandoned.accounts.models import CaiaAbandonedUser
from caiaAbandoned.projects.forms import ProjectForm, ProjectDeleteForm
from caiaAbandoned.projects.models import Project


def show_project_details(request, username, slug):
    project = Project.objects.get(slug=slug)
    owner = CaiaAbandonedUser.objects.get(username=username)
    context = {
        'project': project,
        'owner': owner,
    }
    return render(request, template_name='projects/project-details.html', context=context)


def projects_list(request):
    all_projects = Project.objects.all()
    context = {
        'all_projects': all_projects
    }
    return render(request, template_name='projects/project-list-page.html', context=context)


def add_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        project.save()
        return redirect('projects-list')
    context = {'form': form}
    return render(request, template_name='projects/add-project-page.html', context=context)


def my_projects(request, slug):
    all_projects = Project.objects.all()
    project_is_owned_by_user = all_projects.filter(user=request.user)
    context = {
        'all_houses': project_is_owned_by_user
    }
    return render(request, template_name='projects/my-projects-page.html')


def edit_project(request, username, slug):
    project = Project.objects.get(slug=slug)
    if request.method == "GET":
        form = ProjectForm(instance=project, initial=project.__dict__)
    else:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-details', username, slug)
    context = {'form': form}

    return render(request, template_name='projects/edit-project-page.html', context=context)


def delete_project(request, username, slug):
    project = Project.objects.get(slug=slug)
    if request.method == "POST":
        project.delete()
        return redirect('projects-list')
    form = ProjectDeleteForm(initial=project.__dict__)
    context = {'form': form}

    return render(request, template_name='projects/delete-project-page.html', context=context)

