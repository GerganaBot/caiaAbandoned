
from django.core.validators import MinLengthValidator, URLValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from caiaAbandoned.accounts.models import CaiaAbandonedUser


LOCATIONS = [
    ('Sofia Center', 'Sofia Center'),
    ('Sofia Neighbourhood', 'Sofia Neighbourhood'),
    ('Sofia Municipality', 'Sofia Municipality')
]


class Location(models.Model):
    location = models.CharField(max_length=40, choices=LOCATIONS, unique=True)

    def __str__(self):
        return self.location


class House(models.Model):
    house_location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    house_photo = models.URLField(validators=(URLValidator(),))
    zone_name = models.CharField(max_length=50, validators=[MinLengthValidator(3,)])
    street = models.CharField(max_length=50, validators=[MinLengthValidator(3,)])
    street_number = models.PositiveIntegerField()
    description = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)
    square_meters = models.PositiveIntegerField(validators=[
            MaxValueValidator(1000),
            MinValueValidator(10)
        ])
    floors_number = models.PositiveIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    construction_date = models.DateField()
    is_near_parking = models.BooleanField()
    is_near_park = models.BooleanField()
    is_near_metro = models.BooleanField()
    date_of_publication = models.DateField()
    user = models.ForeignKey(to=CaiaAbandonedUser, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-date_of_publication']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.street}-{self.street_number}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.street



