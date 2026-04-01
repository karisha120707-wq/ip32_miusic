from django.shortcuts import render, redirect
from .models import Genre, Tracks, Artist
from django.shortcuts import render
from .forms import AddGenreform , tracksform, ArtistForm
from django.http import HttpResponse

<<<<<<< HEAD
def add_artists (request):
    if request.method == "POST":
        artists = ArtistForm(request.POST, request.FILES)
        if artists.is_valid():
            artists.save()
            print('OK')
        else:
            print('(((')
        return redirect ('/artists')
    else:
        aform = ArtistForm()
        return render (request, "add_artists.html", {'form': aform } )
=======

>>>>>>> work


def artists (request):
    a = Artist.objects.all()
    return render (request, 'artists.html', {'artists': a})


def deltracks (request, id_track):
    track = Tracks.objects.get(id=id_track)
    track.delete()
    return HttpResponse ('<h1> Песня удалена </h1><br><a href ="/">на главную</a>')
    

def editracks (request, id_track) :
    t = Tracks.objects.get(id=id_track)
    
    if request.method == "POST":
        track= tracksform(request.POST, instance = t)
        if track.is_valid():
            track.save()
        return redirect ('/tracks')
    else:
        tform = tracksform(instance = t)
        return render (request, "add_tracks.html", {'form': tform } )
    
def addtracks (request) :
    if request.method == "POST":
        track = tracksform(request.POST)
        if track.is_valid():
            track.save()
        return redirect ('/tracks')
    else:
        tform = tracksform()
        return render (request, "add_tracks.html", {'form': tform } )

def delgenre (request, id_genre): 
    genre = Genre.objects.get(id=id_genre)
    genre.delete()
    return HttpResponse ('<h1> Жанр удален</h1><br><a href ="/">на главную</a>')


def editgenre (request, id_genre):
    g = Genre.objects.get(id=id_genre)

    if request.method == "POST":
        genre = AddGenreform(request.POST, instance = g)
        if genre.is_valid():
            genre.save()
        return redirect ('/genre')
    else:
        genreform = AddGenreform(instance = g)
        return render (request, "add_genre.html", {'form': genreform } )

def addgenre (request) :
    if request.method == "POST":
        genre = AddGenreform(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect ('/genre')
    else:
        genreform = AddGenreform()
        return render (request, "add_genre.html", {'form': genreform } )


def main (request) :
    return render (request, 'index.html')


def genres (request) :
    genre = Genre.objects.all()
    return render (request, 'genre.html', {'genres': genre})


def tracks (request):
    track = Tracks.objects.all()
    return render (request, 'tracks.html', {'tracks': track})