from django import forms

class MovieSearchForm(forms.Form):
    query = forms.CharField(
        label='Пошук фільму', 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву фільму'
        })
    )
