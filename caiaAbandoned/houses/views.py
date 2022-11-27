from django.shortcuts import render


def add_house(request):
    return render(request, template_name='houses/house-add-page.html')


def show_house_details(request):
    return render(request, template_name='houses/house-details-page.html')


def houses_list(request):
    return render(request, template_name='houses/houses-list.html')
