from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'), # List page as the root
    path('add/', views.add_recipe, name='add_recipe'),
]