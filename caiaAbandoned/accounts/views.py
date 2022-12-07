from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from caiaAbandoned.accounts.forms import CaiaUserCreateForm


def register(request):
    form = CaiaUserCreateForm()

    if request.method == "POST":
        form = CaiaUserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Profile was successfully created for' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, template_name='accounts/register-page.html', context=context)


def login_view(request):
    # form = CaiaLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username='username', password='password')

        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}
    return render(request, template_name='accounts/login-page.html', context=context)


def show_profile_details(request):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')
