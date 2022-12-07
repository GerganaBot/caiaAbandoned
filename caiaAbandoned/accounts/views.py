from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from caiaAbandoned.accounts.forms import CaiaUserCreateForm, CaiaLoginForm

UserModel = get_user_model()


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


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


def show_profile_details(request):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')
