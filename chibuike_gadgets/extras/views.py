from django.shortcuts import render, HttpResponse

# Create your views here.
def aboutus(request):
    return HttpResponse('<div>Some text about us</div>')