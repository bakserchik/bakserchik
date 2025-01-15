from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieSearchForm
from .models import Movie

MOVIES = [
    {
        "title": "Inception",
        "image": "https://www.imdb.com/title/tt1375666/mediaviewer/rm3426651392/?ref_=tt_ov_i",
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
    {
        "title": "The Dark Knight",
        "image": "https://via.placeholder.com/150",
        "description": "A battle between Batman and the Joker in a city on the edge of chaos.",
    },
    {
        "title": "Avatar",
        "image": "https://via.placeholder.com/150",
        "description": "A visually stunning epic about an alien world and its inhabitants.",
    },
    {
        "title": "Pulp Fiction",
        "image": "https://via.placeholder.com/150",
        "description": "A darkly comedic tale of crime, redemption, and fate.",
    },
    {
        "title": "The Shawshank Redemption",
        "image": "https://via.placeholder.com/150",
        "description": "A moving story of hope and friendship in a harsh prison environment.",
    },
    {
        "title": "Forrest Gump",
        "image": "https://via.placeholder.com/150",
        "description": "A heartwarming story of a simple man living an extraordinary life.",
    },
]

def home(request):
    """
    Представлення для домашньої сторінки.
    """
    return render(request, 'home.html', {'movies': MOVIES})

def search(request):
    form = MovieSearchForm(request.POST or None)  
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = [movie for movie in MOVIES if query.lower() in movie["title"].lower()] 

    return render(request, 'search/search.html', {'form': form, 'results': results})

def admin_search(request):
    return HttpResponse("Це сторінка пошуку для адміністратора.")


