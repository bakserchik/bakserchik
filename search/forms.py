from django import forms
from .models import Movie

class MovieSearchForm(forms.Form):
    query = forms.CharField(
        label='Пошук фільму', 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву фільму'
        })
    )


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'year', 'image', 'trailer_url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }

  
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Назва фільму не може бути порожньою!")
        if len(title) < 3:
            raise forms.ValidationError("Назва фільму повинна бути не менше 3 символів.")
        return title

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1900 or year > 2100:
            raise forms.ValidationError("Рік має бути в межах від 1900 до 2100.")
        return year


