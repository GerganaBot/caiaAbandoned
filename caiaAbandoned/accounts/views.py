from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, DeleteView

from caiaAbandoned.accounts.forms import CaiaUserCreateForm, CaiaUserEditForm
from caiaAbandoned.accounts.models import CaiaAbandonedUser


def register(request):
    form = CaiaUserCreateForm()

    if request.method == "POST":
        form = CaiaUserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    context = {'form': form}
    return render(request, template_name='accounts/register-page.html', context=context)


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('home-page')


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
