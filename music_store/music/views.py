from django.shortcuts import render
from .models import Artist, Album

# Create your views here.

def home(request):
    """View for the home page."""
    return render(request, 'home.html')

def artist_list(request):
    """View to display all artists, ordered by debut year."""
    artists = Artist.objects.all().order_by('debut_year')
    context = {'artists': artists}
    return render(request, 'artist_list.html', context)

def album_list(request):
    """View to display all albums, ordered by release date."""
    albums = Album.objects.all().order_by('release_date')
    context = {'albums': albums}
    return render(request, 'album_list.html', context)