from django.shortcuts import render, redirect

from caiaAbandoned.common.forms import SearchForm
from caiaAbandoned.houses.models import House, Location


def home_page(request):
    all_locations = House.objects.all()
    search_form = SearchForm()

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_locations = all_locations.filter(
                zone_name__icontains=search_form.cleaned_data['zone_name'])
            context = {
                'object_list': all_locations
            }
            return render(request, template_name='houses/houses-list.html', context=context)

    context = {
        'search_form': search_form,
    }
    return render(request, template_name='common/home-page.html', context=context)


def about_us(request):
    return render(request, template_name='common/about-us.html')








