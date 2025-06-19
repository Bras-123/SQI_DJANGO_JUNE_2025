from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Album
from .form import ArtistCreateForm, AlbumCreateNotModelForm


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

def artist_detail(request, pk):
    """View for a single artist's detail page."""
    artist= get_object_or_404(Artist, pk=pk)
    context = {'artist':artist}
    return render (request,'artist_detail.html', context)

def album_detail(request, pk):
    """View for a single album's detail page."""
    album = get_object_or_404(Album, pk=pk)
    context = {'album': album}
    return render(request, 'album_detail.html', context)

def create_artist(request):
    artist_create_form= ArtistCreateForm()
    if request.method == "POST":
        artist_create_form= ArtistCreateForm(request.POST, request.FILES)
        if artist_create_form.is_valid():
            artist_create_form.save()
            return redirect('music:artist_list')
    context = {
        "create_form": artist_create_form
    }
    return render(request,'artist_form.html',context)

def create_album_no_model_form(request):
    no_model_album_form = AlbumCreateNotModelForm()
    if request.method == "POST":
        no_model_album_form = AlbumCreateNotModelForm(request.POST, request.FILES)
        if no_model_album_form.is_valid():
            cleaned_data = no_model_album_form.cleaned_data
            Album.objects.create(**cleaned_data)
            return redirect('music:album_list')
    context = {
        'form': no_model_album_form
    }
    return render(request, "create-album.html", context)