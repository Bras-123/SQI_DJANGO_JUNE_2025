from django.db import models

from django.core.validators import MinValueValidator

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(validators=[MinValueValidator(3)]) # Time in minutes
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    # Use a default image if no cover image is provided
    cover_image = models.ImageField( upload_to='recipe_covers/',default='defaults/default_cover.jpg')

    def __str__(self):
        return self.name