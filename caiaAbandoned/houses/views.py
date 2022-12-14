from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from caiaAbandoned.accounts.models import CaiaAbandonedUser
from caiaAbandoned.common.utils import is_owner
from caiaAbandoned.houses.forms import HouseForm, HouseDeleteForm
from caiaAbandoned.houses.models import House
from caiaAbandoned.projects.models import Project


@login_required
def add_house(request):
    form = HouseForm(request.POST or None)
    if form.is_valid():
        house = form.save(commit=False)
        house.user = request.user
        house.save()
        return redirect('houses-list')
    context = {'form': form}
    return render(request, template_name='houses/house-add-page.html', context=context)


def show_house_details(request, slug):
    house = get_object_or_404(House, slug=slug)
    projects = Project.objects.all()
    project_is_of_the_house = projects.filter(house=house)
    owner = None
    if request.user.is_authenticated:
        owner = CaiaAbandonedUser.objects.get(username=request.user.username)

    context = {
        'house': house,
        'owner': owner,
        'projects': project_is_of_the_house
    }
    return render(request, template_name='houses/house-details-page.html', context=context)


class HousesList(ListView):
    model = House
    template_name = 'houses/houses-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def my_houses(request, slug):
    all_houses = House.objects.all()
    house_is_owned_by_user = all_houses.filter(user=request.user)
    context = {
        'all_houses': house_is_owned_by_user
    }
    return render(request, template_name='houses/my-houses-page.html', context=context)


@login_required
def edit_house(request, slug):
    house = get_object_or_404(House, slug=slug)
    if not is_owner(request, house):
        return redirect('house-details', slug=slug)
    if request.method == "GET":
        form = HouseForm(instance=house, initial=house.__dict__)
    else:
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house-details', slug)
    context = {'form': form}

    return render(request, template_name='houses/edit-house-page.html', context=context)


@login_required
def delete_house(request, slug):
    try:
        house = House.objects.get(slug=slug)
    except House.DoesNotExist:
        raise Http404("No house matches the given query.")

    if not is_owner(request, house):
        return redirect('house-details', slug=slug)
    if request.method == "POST":
        house.delete()
        return redirect('houses-list')
    form = HouseDeleteForm(initial=house.__dict__)
    context = {'form': form}

    return render(request, template_name='houses/delete-house-page.html', context=context)
