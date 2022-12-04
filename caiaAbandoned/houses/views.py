from django.shortcuts import render, redirect
from caiaAbandoned.houses.forms import HouseForm
from caiaAbandoned.houses.models import House


def add_house(request):
    form = HouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('houses-list')
    context = {'form': form}
    return render(request, template_name='houses/house-add-page.html', context=context)


def show_house_details(request, slug):
    house = House.objects.get(slug=slug)
    context = {
        'house': house,
    }
    return render(request, template_name='houses/house-details-page.html', context=context)


def houses_list(request):
    all_houses = House.objects.all()
    context = {
        'all_houses': all_houses
    }
    return render(request, template_name='houses/houses-list.html', context=context)


def my_houses(request):
    return render(request, template_name='houses/my-houses-page.html')


def edit_house(request, slug):
    house = House.objects.get(slug=slug)
    if request.method == "GET":
        form = HouseForm(instance=house, initial=house.__dict__)
    else:
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house-details', slug)
    context = {'form': form}

    return render(request, template_name='houses/edit-house-page.html', context=context)

