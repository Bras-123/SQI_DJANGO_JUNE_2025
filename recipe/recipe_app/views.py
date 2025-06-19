from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe
# Create your views here.

def add_recipe(request):
    """View function to add a new recipe."""
    if request.method == 'POST':
        # Form was submitted
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Save the new recipe to the database
            return redirect('recipe_list') # Redirect to the recipe list page
    else:
        # Display a blank form for a GET request
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'add_recipe.html', context)

def recipe_list(request):
    """View function to display all recipes."""
    recipes = Recipe.objects.all().order_by('name')
    context = {'recipes': recipes}
    return render(request, 'recipe_list.html', context)
    
