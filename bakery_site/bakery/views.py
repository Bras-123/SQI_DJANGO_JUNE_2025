from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'bakery/home.html')

def about(request):
    return render(request, 'bakery/about.html')

def menu(request):
    return render(request, 'bakery/menu.html')

def contact(request):
    return render(request, 'bakery/contact.html')
