from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Artist)
admin.site.register(models.Album)