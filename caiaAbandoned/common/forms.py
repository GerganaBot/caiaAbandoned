from django import forms


class SearchForm(forms.Form):
    zone_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by zone...'
            }
        )
    )
