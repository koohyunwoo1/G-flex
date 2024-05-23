from rest_framework import serializers
from movies.models import Movie
from django.contrib.auth import get_user_model

# 유저 프로필을 가져오기 위한 serializer
User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
   
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'pk', 'id')
    
    # 좋아요를 누른 영화를 알기 위해 필요
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = ('like_movies','pk','username', 'id')