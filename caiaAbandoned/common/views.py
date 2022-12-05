from django.shortcuts import render, redirect

from caiaAbandoned.common.forms import SearchForm
from caiaAbandoned.houses.models import House, Location


def home_page(request):
    return render(request, template_name='common/home-page.html')


def about_us(request):
    return render(request, template_name='common/about-us.html')


def search_page(request):
    all_locations = House.objects.all()
    search_form = SearchForm()

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            print(search_form.cleaned_data)
            all_locations = all_locations.filter(
                street__icontains=search_form.cleaned_data['street'])
            context = {
                'all_houses': all_locations
            }
            return render(request, template_name='houses/houses-list.html', context=context)

    context = {
        'search_form': search_form,
    }
    return render(request, template_name='common/search-page.html', context=context)





