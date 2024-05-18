from django.contrib import admin

# Register your models here.
from .models import Movie, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'words', 'like_users', 'release_date', 'genres', 'poster_url', )



admin.site.register(Movie)
admin.site.register(Comment)