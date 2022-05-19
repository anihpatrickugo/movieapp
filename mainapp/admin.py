from django.contrib import admin
from .models import *

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'upload_date']
    ordering = ['tittle']
    prepopulated_fields = {"slug": ("tittle",)}






class UpcomingMovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tittle",)}
    ordering = ['release_date']





admin.site.register(Movie, MovieAdmin)
admin.site.register(UpcomingMovie, UpcomingMovieAdmin)

admin.site.register(Genre)
