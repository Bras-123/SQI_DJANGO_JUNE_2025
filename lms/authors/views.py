from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def all_authors(request):
    return render(request, "authors/authors.html")
    

def book_signings(request):
    return render(request,"authors/booking-singings.html")