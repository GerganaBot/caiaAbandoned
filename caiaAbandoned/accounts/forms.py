from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from caiaAbandoned.accounts.models import CaiaAbandonedUser


class CaiaUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaiaAbandonedUser
        fields = ('username', 'email', 'password1', 'password2')


# class CaiaLoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
#     password = forms.CharField(
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'})
#     )



