from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieSearchForm 
from .models import Movie

MOVIES = [
    {
        "title": "Inception",
        "image": "https://via.placeholder.com/150",
        "description": "A mind-bending thriller about dream invasion.",
    },
    {
        "title": "The Matrix",
        "image": "https://via.placeholder.com/150",
        "description": "A hacker discovers the shocking truth about his reality.",
    },
    {
        "title": "Interstellar",
        "image": "https://via.placeholder.com/150",
        "description": "An epic journey to save humanity by exploring the stars.",
    },
]

def search(request):
    form = MovieSearchForm(request.POST or None)  
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = [movie for movie in MOVIES if query.lower() in movie["title"].lower()] 

    return render(request, 'search/search.html', {'form': form, 'results': results})

def admin_search(request):
    return HttpResponse("Це сторінка пошуку для адміністратора.")

