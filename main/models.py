from django.db import models

class Artist (models.Model):
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', null=True)

    def __str__(self):
        return self.name



class Genre(models.Model):
    name_ru = models.CharField(max_length=500)
    name_an = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name_ru

    
class Tracks(models.Model):
    title = models.CharField(max_length=500)
    duration = models.IntegerField(max_length=500)
    genre =  models.ManyToManyField(Genre)
    artists =models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)
    def __str__(self):
        return self.title