from django.shortcuts import render
from .models import Author
from library.models import Book

# Create your views here.
from django.http import HttpResponse

def all_authors(request):
    return render(request, "authors/authors.html")
    

def book_signings(request):
    return render(request,"authors/booking-singings.html")

def mvt(request):
    authors_dob = Author.objects.order_by("birth_date")
    authors = Author.objects.all()
    books = Book.objects.order_by("-title")
    context = {
        "authors_dob": authors_dob,
        "authors": authors,
        "books": books,
    }
    return render(request, "authors/mvt.html", context)