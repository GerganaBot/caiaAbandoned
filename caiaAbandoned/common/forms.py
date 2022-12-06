from django import forms


class SearchForm(forms.Form):
    street = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by street name...'
            }
        )
    )
