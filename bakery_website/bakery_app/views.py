from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'bakery_app/home.html')

def about(request):
    return render(request, 'bakery_app/about.html')

def menu(request):
    menu_items = {
        'Breads': [
            {'name': 'Classic Sourdough', 'price': '₦3,500'},
            {'name': 'Multigrain Loaf', 'price': '₦3,000'},
            {'name': 'Baguette', 'price': '₦1,500'},
        ],
        'Pastries': [
            {'name': 'Butter Croissant', 'price': '₦1,800'},
            {'name': 'Chocolate Chip Cookie', 'price': '₦1,200'},
            {'name': 'Cinnamon Roll', 'price': '₦2,000'},
        ]
    }
    return render(request, 'bakery_app/menu.html', {'menu_items': menu_items})

def contact(request):
    return render(request, 'bakery_app/contact.html')