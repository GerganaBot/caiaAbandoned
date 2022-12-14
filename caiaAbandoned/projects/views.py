from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from caiaAbandoned.accounts.models import CaiaAbandonedUser
from caiaAbandoned.common.utils import is_owner
from caiaAbandoned.houses.models import House
from caiaAbandoned.projects.forms import ProjectForm, ProjectDeleteForm
from caiaAbandoned.projects.models import Project


def show_project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    owner = None
    if request.user.is_authenticated:
        owner = CaiaAbandonedUser.objects.get(username=request.user.username)
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


@login_required
def add_project(request, slug):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        house = House.objects.get(slug=slug)
        project.house = house
        project.save()
        return redirect('projects-list')
    context = {'form': form}
    return render(request, template_name='projects/add-project-page.html', context=context)


@login_required
def my_projects(request, slug):
    all_projects = Project.objects.all()
    project_is_owned_by_user = all_projects.filter(user=request.user)
    context = {
        'all_projects': project_is_owned_by_user
    }
    return render(request, template_name='projects/my-projects-page.html', context=context)


@login_required
def edit_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if not is_owner(request, project):
        return redirect('project-details', slug=slug)
    if request.method == "GET":
        form = ProjectForm(instance=project, initial=project.__dict__)
    else:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-details', slug)
    context = {'form': form}

    return render(request, template_name='projects/edit-project-page.html', context=context)


@login_required
def delete_project(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("No project matches the given query.")

    if not is_owner(request, project):
        return redirect('project-details', slug=slug)
    if request.method == "POST":
        project.delete()
        return redirect('projects-list')
    form = ProjectDeleteForm(initial=project.__dict__)
    context = {'form': form}

    return render(request, template_name='projects/delete-project-page.html', context=context)

