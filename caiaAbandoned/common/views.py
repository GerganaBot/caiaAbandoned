from django.shortcuts import render


def home_page(request):
    return render(request, template_name='common/home-page.html')


def about_us(request):
    return render(request, template_name='common/about-us.html')





