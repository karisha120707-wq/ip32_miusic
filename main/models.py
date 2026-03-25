from django.db import models


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
    def __str__(self):
        return self.title