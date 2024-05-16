from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'words', 'like_users', 'release_date', 'genres', 'poster_url', )



admin.site.register(Movie)