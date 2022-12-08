from django import views
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, DeleteView

from caiaAbandoned.accounts.forms import CaiaUserCreateForm, CaiaLoginForm, CaiaUserEditForm
from caiaAbandoned.accounts.models import CaiaAbandonedUser


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


class SignOutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('login')


class UserDetailsView(DetailView):
    model = CaiaAbandonedUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserEditView(UpdateView):
    model = CaiaAbandonedUser
    form_class = CaiaUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserDeleteView(DeleteView):
    model = CaiaAbandonedUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home-page')
