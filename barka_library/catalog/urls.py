from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("special/", views.special_books, name="special_books"),
]