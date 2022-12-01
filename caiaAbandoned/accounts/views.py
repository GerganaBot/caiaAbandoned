from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render


def login(request):
    return render(request, template_name='accounts/login-page.html')


def register(request):
    return render(request, template_name='accounts/register-page.html')


def show_profile_details(request):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')
