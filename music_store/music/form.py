from django import forms

from .models import Artist,Album

class ArtistCreateForm(forms.ModelForm):
    class Meta:
        model = Artist

        fields = "__all__"


class AlbumCreateNotModelForm(forms.Form):
    title = forms.CharField(max_length=100)
    release_date = forms.DateField()
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    album_cover = forms.ImageField(required=False)