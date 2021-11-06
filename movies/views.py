from django.shortcuts import render
from django.http import Http404
from .models import Movie


# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context)


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        context = {
            "movie": movie
        }
    except Movie.DoesNotExist:
        raise Http404("Movie has not found!")
    return render(request, 'movies/detail.html', context)


def search(request):
    return render(request, 'movies/search.html')
