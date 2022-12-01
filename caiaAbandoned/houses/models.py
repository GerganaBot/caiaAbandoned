from django.db import models


LOCATIONS = [
    ('Center', 'Sofia Center'),
    ('Neighbourhood', 'Sofia Neighbourhood'),
    ('Municipality', 'Sofia Municipality')
]


class Locations(models.Model):
    location = models.CharField(max_length=40, choices=LOCATIONS)


class Houses(models.Model):
    house_location = models.ForeignKey(to=Locations, on_delete=models.CASCADE)
    house_photo = models.URLField()
    street = models.CharField(max_length=50)
    street_number = models.PositiveIntegerField()
    description = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True)





