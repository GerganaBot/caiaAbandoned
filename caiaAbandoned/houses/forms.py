from django import forms
from caiaAbandoned.houses.models import House


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['house_location', 'house_photo', 'zone_name', 'street', 'street_number', 'description', 'square_meters',
                  'floors_number', 'construction_date', 'is_near_parking', 'is_near_park', 'is_near_metro', 'date_of_publication']
        widgets = {
            'house_location': forms.RadioSelect(),
            'house_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
            'zone_name': forms.TextInput(attrs={'placeholder': 'Zone/neighbourhood/town name'}),
            'street': forms.TextInput(attrs={'placeholder': 'Street'}),
            'street_number': forms.NumberInput(attrs={'placeholder': 'Street number'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'square_meters': forms.NumberInput(attrs={'placeholder': 'Square meters'}),
            'floors_number': forms.NumberInput(attrs={'placeholder': 'Floors number'}),
            'construction_date': forms.DateInput(attrs={'type': 'date'}),
            'is_near_parking': forms.CheckboxInput(),
            'is_near_park': forms.CheckboxInput(),
            'is_near_metro': forms.CheckboxInput(),
            'date_of_publication': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'is_near_parking': 'Near parking:',
            'is_near_park': 'Near park:',
            'is_near_metro': 'Near metro:',
        }


class HouseDeleteForm(HouseForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


