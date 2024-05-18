from rest_framework import serializers
from movies.models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
   
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = ('like_movies','pk','username', 'id')