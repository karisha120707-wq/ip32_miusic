from django import forms
from .models import Genre, Tracks

class AddGenreform(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_ru', 'name_an', 'description']
        labels = {
            'name_ru' : 'Название на русском',
            'name_an' : 'Название на английском',
            'description' : 'Описание'
        }

class tracksform(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = '__all__'
        labels = {
            'genre' : 'Напишите название жанра',
            'name_tracks' : 'Напишите название песни',
            'duration' : 'Продолжительность'
        }


class ArtistForm (forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labes = {
            'name' : 'Имя / название',
            'image' : 'Фотография'
        }
