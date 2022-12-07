from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from caiaAbandoned.accounts.models import CaiaAbandonedUser


class CaiaUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaiaAbandonedUser
        fields = ('username', 'email', 'password1', 'password2')


class CaiaLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'})
    )


class CaiaUserEditForm(forms.ModelForm):
    class Meta:
        model = CaiaAbandonedUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password',)
        labels = {
            'username': 'Username:',
            'first_name': 'First name:',
            'last_name': 'Last name:',
            'email': 'Email:',
            'profile_picture': 'Image:',
            'gender': 'Gender'
        }




