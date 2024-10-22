from django.db import models
from django.conf import settings
import datetime

# 배우
class Actor(models.Model):
    name = models.CharField(max_length=30, null=False)
    profile_path = models.TextField(null=True)
    
    def __str__(self):
        return self.name

# 장르
class Genre(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

# 무드 태그
class MoodTag(models.Model):
    name = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.name

# 영화
class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    moodtag = models.ManyToManyField(MoodTag, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=300)
    overview = models.TextField()
    budget = models.BigIntegerField()
    popularity = models.FloatField()
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True, default=datetime.date.today)
    revenue = models.BigIntegerField()
    runtime = models.IntegerField(null=True)
    tagline = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    words = models.TextField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    def __str__(self):
        return self.title


# 댓글
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
