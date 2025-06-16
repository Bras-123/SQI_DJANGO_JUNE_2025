from django.shortcuts import render

# Create your views here.
def availabe_dishes(request):
    return render(request, 'menu/dishes.html')
