from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'cooking_time', 'image', 'cover_image']

        # Optional: Customize widgets if needed
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4, 'placeholder': 'e.g., 2 cups flour, 1 cup sugar, ...'}),
            'instructions': forms.Textarea(attrs={'rows': 6}),
        }