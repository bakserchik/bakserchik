from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Movie, UserProfile
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Movie
from search.forms import MovieForm, MovieSearchForm


MOVIES = [
    {
        "id": 1,
        "title": "Inception",
        "image": "https://s9.vcdn.biz/static/f/1396166031/image.jpg",
        "description": "A mind-bending thriller about dream invasion.",
        "genre": "Sci-Fi, Thriller",
        "year": 2010,
        "trailer_url": "https://www.youtube.com/embed/YoHD9XEInc0", 
    },
    {
        "id":2,
        "title": "The Matrix",
        "image": "https://filmartgallery.com/cdn/shop/products/The-Matrix-Vintage-Movie-Poster-Original-French-1-panel-47x63.jpg?v=1680238937",
        "description": "A hacker discovers the shocking truth about his reality.",
        "genre": "Sci-Fi, Action",
        "year": 1999,
        "trailer_url": "https://www.youtube.com/embed/vKQi3bBA1y8",
    },
    {
        "id":3,
        "title": "Interstellar",
        "image": "https://m.media-amazon.com/images/I/91vIHsL-zjL.jpg",
        "description": "An epic journey to save humanity by exploring the stars.",
        "genre": "Sci-Fi, Drama",
        "year": 2014,
        "trailer_url": "https://www.youtube.com/embed/zSWdZVtXT7E",
    },
    {
        "id":4,
        "title": "The Dark Knight",
        "image": "https://www.prime1studio.com/on/demandware.static/-/Sites-p1s-master-catalog/default/dw91bf350b/images/HDMMDC-02/media/hdmmdc-02_ogp_1.jpg",
        "description": "A battle between Batman and the Joker in a city on the edge of chaos.",
        "genre": "Action, Crime, Drama",
        "year": 2008,
        "trailer_url": "https://www.youtube.com/embed/EXeTwQWrcwY",
    },
    {
        "id":5,
        "title": "Avatar",
        "image": "https://resizing.flixster.com/f0bXqQUdQ0m6fyqZjI1OXSEia9E=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzEzYmY3ZmZiLWMzYjEtNDQxMy05NTAxLTc2YTRlNmE3NWY2MC5qcGc=",
        "description": "A visually stunning epic about an alien world and its inhabitants.",
        "genre": "Sci-Fi, Adventure",
        "year": 2009,
        "trailer_url": "https://www.youtube.com/embed/5PSNL1qE6VY",
    },
    {
        "id":6,
        "title": "Pulp Fiction",
        "image": "https://www.theoriginalunderground.com/cdn/shop/files/pulp-fiction-film-poster-print-591645_1200x1200.jpg?v=1729110869",
        "description": "A darkly comedic tale of crime, redemption, and fate.",
        "genre": "Crime, Drama",
        "year": 1994,
        "trailer_url": "https://www.youtube.com/embed/s7EdQ4FqbhY",
    },
    {
        "id":7,
        "title": "The Shawshank Redemption",
        "image": "https://i.scdn.co/image/ab67616d0000b273e710c1f5b228046932790031",
        "description": "A moving story of hope and friendship in a harsh prison environment.",
        "genre": "Drama",
        "year": 1994,
        "trailer_url": "https://www.youtube.com/embed/6hB3S9bIaco",
    },
    {
        "id":8,
        "title": "Forrest Gump",
        "image": "https://m.media-amazon.com/images/S/pv-target-images/f9ddd832d1b566f5b8dd29a4dbc76b7531c420c8c8d9fdfe94eca128bda8e2b1.jpg",
        "description": "A heartwarming story of a simple man living an extraordinary life.",
        "genre": "Drama, Romance",
        "year": 1994,
        "trailer_url": "https://www.youtube.com/embed/bLvqoHBptjg",
    },
]


def toggle_favorite(request, movie_id):
    """
    Додавання/видалення фільму з вибраних.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    profile = UserProfile.objects.get(user=request.user)

    if movie in profile.favorite_movies.all():
        profile.favorite_movies.remove(movie)
    else:
        profile.favorite_movies.add(movie)

    return redirect('favorite_list')  # Перехід до списку вибраних фільмів

def favorite_list(request):
    """
    Виведення вибраних фільмів.
    """
    films = Movie.objects.filter(favorite_by_users=True)  # Вибрані фільми поточного користувача
    return render(request, 'favorite.html', {'films': films})



def home(request):
    print("uftjy")
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

def add_movie(request):
    """
    Представлення для додавання фільму.
    """
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()  
            return redirect('home')   
    else:
        form = MovieForm() 

    return render(request, 'add_movie.html', {'form': form})

def add_to_cart(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    cart = request.session.get('cart', [])

    if movie.id not in cart:
        cart.append(movie.id)

    request.session['cart'] = cart
    return redirect('view_cart')

def movie_list(request):
    movie = Movie.objects.all()
    return render(request, 'search/movie_list.html',{'movie_list':movie})


def view_cart(request):
    cart = request.session.get('cart', [])
    movies_in_cart = Movie.objects.filter(id__in=cart)

    return render(request, 'view_cart.html', {'movies_in_cart': movies_in_cart})


def toggle_favorite(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.is_favorite = not film.is_favorite  
    film.save()
   
    return redirect('favorite_list')  
 
def favorite_list(request):
    films = Film.objects.filter(is_favorite=True)  
    return render(request, 'favorite.html', {'films': films})






