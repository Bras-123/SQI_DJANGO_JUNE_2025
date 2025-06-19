from django.db import models
from django.core.validators import MinLengthValidator

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone


# Custom validator for the album's release date
def validate_release_year(value):
    current_year = timezone.now().year
    if value.year < 1800 or value.year > current_year:
        raise ValidationError(
            f'Release year must be between 1800 and {current_year}.'
        )
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    debut_year = models.IntegerField()
    artist_image = models.ImageField(upload_to='artist_image/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Album(models.Model):
    title = models.CharField(max_length=100,validators=[MinLengthValidator(2)])
    release_date = models.DateField(validators=[validate_release_year])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    album_cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)

    def __str__(self):
        return f'{self.title} by {self.artist.name}'
