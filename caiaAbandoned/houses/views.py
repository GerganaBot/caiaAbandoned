from django.shortcuts import render

from caiaAbandoned.houses.models import House


def add_house(request):
    return render(request, template_name='houses/house-add-page.html')


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
