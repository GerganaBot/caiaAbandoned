from django.contrib.auth.forms import UserCreationForm
from caiaAbandoned.accounts.models import CaiaAbandonedUser


class CaiaUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaiaAbandonedUser
        fields = ('username', 'email', 'password1', 'password2')





