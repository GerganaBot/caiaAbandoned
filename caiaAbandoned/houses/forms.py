from django import forms
from caiaAbandoned.houses.models import House


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['house_location', 'house_photo', 'street', 'street_number', 'description', 'square_meters',
                  'floors_number', 'construction_date', 'is_near_parking', 'is_near_park', 'is_near_metro', 'date_of_publication']

