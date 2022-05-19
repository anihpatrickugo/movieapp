from audioop import reverse
import numbers
from unicodedata import name
from django.db import models
from django.urls import reverse


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name





class Movie(models.Model):
    tittle      = models.CharField(max_length=250)
    cover_photo = models.ImageField(upload_to='movie_covers/')
    video       = models.FileField(upload_to='movie_covers/')
    genre       = models.ManyToManyField(Genre)
    description = models.TextField(max_length=300, null=True)
    duration    = models.DurationField(null=True)
    upload_date = models.DateField(auto_now=True)
    slug        = models.SlugField(null=True)

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'slug': self.slug})

    


class UpcomingMovie(models.Model):
    tittle      = models.CharField(max_length=250)
    cover_photo = models.ImageField(upload_to='upcoming_covers/')
    video       = models.FileField(upload_to='upcoming_covers/')
    genre       = models.ManyToManyField(Genre)
    description = models.TextField(max_length=300)
    release_date = models.DateField()
    slug        = models.SlugField()

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('upcoming-detail', kwargs={'slug': self.slug})


















