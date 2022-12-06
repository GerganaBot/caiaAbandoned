from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Do not show', 'Do not show')
]


class CaiaAbandonedUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.URLField()
    gender = models.CharField(max_length=12, choices=GENDER)








