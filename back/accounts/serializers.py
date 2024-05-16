from rest_framework import serializers
from articles.models import Article
from movies.models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    
    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = '__all__'

    
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'


    
    like_articles = ArticleSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ('like_articles','like_movies','articles','pk','username')