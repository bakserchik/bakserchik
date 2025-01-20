from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieSearchForm
from .models import Movie

MOVIES = [
    {
        "title": "Inception",
        "image": "https://s9.vcdn.biz/static/f/1396166031/image.jpg",
        "description": "A mind-bending thriller about dream invasion.",
        "genre": "Sci-Fi, Thriller",
        "year": 2010,
        "trailer_url": "https://www.youtube.com/embed/YoHD9XEInc0",  # YouTube trailer link
    },
    {
        "title": "The Matrix",
        "image": "https://filmartgallery.com/cdn/shop/products/The-Matrix-Vintage-Movie-Poster-Original-French-1-panel-47x63.jpg?v=1680238937",
        "description": "A hacker discovers the shocking truth about his reality.",
        "genre": "Sci-Fi, Action",
        "year": 1999,
        "trailer_url": "https://www.youtube.com/embed/vKQi3bBA1y8",
    },
    {
        "title": "Interstellar",
        "image": "https://m.media-amazon.com/images/I/91vIHsL-zjL.jpg",
        "description": "An epic journey to save humanity by exploring the stars.",
        "genre": "Sci-Fi, Drama",
        "year": 2014,
        "trailer_url": "https://www.youtube.com/embed/zSWdZVtXT7E",
    },
    {
        "title": "The Dark Knight",
        "image": "https://www.prime1studio.com/on/demandware.static/-/Sites-p1s-master-catalog/default/dw91bf350b/images/HDMMDC-02/media/hdmmdc-02_ogp_1.jpg",
        "description": "A battle between Batman and the Joker in a city on the edge of chaos.",
        "genre": "Action, Crime, Drama",
        "year": 2008,
        "trailer_url": "https://www.youtube.com/embed/EXeTwQWrcwY",
    },
    {
        "title": "Avatar",
        "image": "https://resizing.flixster.com/f0bXqQUdQ0m6fyqZjI1OXSEia9E=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzEzYmY3ZmZiLWMzYjEtNDQxMy05NTAxLTc2YTRlNmE3NWY2MC5qcGc=",
        "description": "A visually stunning epic about an alien world and its inhabitants.",
        "genre": "Sci-Fi, Adventure",
        "year": 2009,
        "trailer_url": "https://www.youtube.com/embed/5PSNL1qE6VY",
    },
    {
        "title": "Pulp Fiction",
        "image": "https://www.theoriginalunderground.com/cdn/shop/files/pulp-fiction-film-poster-print-591645_1200x1200.jpg?v=1729110869",
        "description": "A darkly comedic tale of crime, redemption, and fate.",
        "genre": "Crime, Drama",
        "year": 1994,
        "trailer_url": "https://www.youtube.com/embed/s7EdQ4FqbhY",
    },
    {
        "title": "The Shawshank Redemption",
        "image": "https://i.scdn.co/image/ab67616d0000b273e710c1f5b228046932790031",
        "description": "A moving story of hope and friendship in a harsh prison environment.",
        "genre": "Drama",
        "year": 1994,
        "trailer_url": "https://www.youtube.com/embed/6hB3S9bIaco",
    },
    {
        "title": "Forrest Gump",
        "image": "https://m.media-amazon.com/images/S/pv-target-images/f9ddd832d1b566f5b8dd29a4dbc76b7531c420c8c8d9fdfe94eca128bda8e2b1.jpg",
        "description": "A heartwarming story of a simple man living an extraordinary life.",
        "genre": "Drama, Romance",
        "year": 1994,
        "trailer_url": "https://www.youtube.com/embed/bLvqoHBptjg",
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


