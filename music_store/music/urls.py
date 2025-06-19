from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artist_list, name='artist_list'),
    path('albums/', views.album_list, name='album_list'),
    path('artists/artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('albums/album/<int:pk>/', views.album_detail, name='album_detail'),
    path('add_artist/',views.create_artist,name='create_artist'),
    path('create/album/manual-render/', views.create_album_no_model_form, name='create_album_no_model_form')
    
]