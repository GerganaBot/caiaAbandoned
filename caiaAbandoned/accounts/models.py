from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Do not show', 'Do not show')
]


class CaiaAbandonedUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.URLField()
    gender = models.CharField(max_length=12, choices=GENDER)

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username




