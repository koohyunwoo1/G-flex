
from rest_framework import serializers
from .models import Actor, Genre, MoodTag, Movie

from django.contrib.auth import get_user_model

from random import sample

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname')

# 로그인 후 맨 처음 페이지에 인기순으로 3개의 영화를 나타내기 위한 seri~

# vote_average 이게 평점임

class MovieHomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'vote_average', 'overview', 'poster_path')
        # 출력할 필드는 제목과 평점만


# 사용자가 좋아요 누른 영화
        
class UserLikeMovieListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'words',)
    
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_movies',)


# 검색한 영화와 비슷한 영화

class MovieSearchSerializer(serializers.ModelSerializer):
    similarity = serializers.FloatField(default = 0)
    
    class Meta:

        model = Movie
        fields = ('pk', 'words', 'title', 'poster_path', 'similarity')

# 여러 영화 제공
        
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Movie
        fields = ('pk', 'words')
    
# 사용자가 선택 또는 좋아요 한 영화와 비슷한 영화
        
class UserChoiceSimilarMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk','title', 'poster_path')

# 단일 영화 상세 정보
        
class MovieDetailSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
        
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)

    like_movies = UserSerializer(read_only=True, many=True)
    

    class Meta:
        model = Movie
        exclude = ('popularity', 'tagline', 'vote_average', 'vote_count', 'words',)

# movie 관련 serializer 완


# 장르 상세 정보
class GenreSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'tagline',)
    
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'

# 장르 전체 조회
class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'pk',)

# 장르 관련 serializer 완
        

# 배우 목록 정보
# class ActorListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = '__all__'

# 단일 배우 detail 정보
        
# class ActorDetailSerializer(serializers.ModelSerializer):

#     class MovieSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Movie
#             fields = ('title', 'poster_path',)
    
#     movie = MovieSerializer(many=True, read_only=True)

#     class Meta:
#         model = Actor
#         fields = ('name', 'movies')

# Mood 태그 상세 정보

class MoodTagSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'tagline',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = MoodTag
        fields = '__all__'

# Mood 전체 태그 가져오기
class MoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoodTag
        fields = '__all__'

# 무드 관련 serializer 완
