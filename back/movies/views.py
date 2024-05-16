from django.shortcuts import render
from .models import Actor, Genre, Movie, MoodTag
from .serializers import UserSerializer, MovieSearchSerializer, MovieListSerializer, UserChoiceSimilarMovieSerializer, MovieDetailSerializer, GenreSerializer, MoodTagSerializer, MovieHomeSerializer, UserLikeMovieListSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_list_or_404, get_object_or_404


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from jellyfish import jaro_winkler_similarity



User = get_user_model()

# 로그인 하고 맨 처음 페이지에 인기순으로 3가지 영화가 뜨게 만드는 함수
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):

    movies = Movie.objects.order_by('-vote_average')[:3]
    serializer = MovieHomeSerializer(movies, many=True)

    return Response(serializer.data)


# 각 영화의 detail 페이지
@api_view(['GET'])
def movie_detail(request, movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie,)

    return Response(serializer.data)

# 영화 검색
@api_view(['GET'])
def search_movie(request, movie_name):

    movies = get_list_or_404(Movie)

    serializer = MovieSearchSerializer(movies, many=True)

    serializer = serach(serializer.data, movie_name)
    return Response(serializer[:10])

# 좋아요 한 영화
@api_view(['POST'])
def like_movie(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    else:
        movie.like_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

# 좋아요 한 영화를 기반으로 추천?
@api_view(['GET'])
def user_like_movie(request, user_pk):
    user = get_object_or_404(User, pk = user_pk)
    serializer = UserLikeMovieListSerializer(user)

    movies = get_list_or_404(Movie)
    movies_serializer = MovieListSerializer(movies, many=True)

    # user가 좋아요한 영화 key값 담기
    movie_key = [data['pk'] for data in serializer.data.get('like_movies')]

    # user가 좋아요 한 영화 index 담기
    idx = []
    for key in movie_key:
        for i in range(len(movies_serializer.data)):
            if key == movies_serializer.data[i]['pk']:
                idx.append(i)
                break
    # words 담기
    xMovie = [data.get('words') for data in movies_serializer.data]

    # 유사 영화 pk 반환
    result = recommend_movies_names(xMovie, idx, movies_serializer)

    # 유사 영화 pk 기반 querySet 생성
    final_movie = [get_object_or_404(Movie, pk=i) for i in result]
    final_serializer = UserChoiceSimilarMovieSerializer(final_movie, many=True)

    return Response(final_serializer.data)

@api_view(['GET'])
def similar_movie(request,movie_pk):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)

    idx = []
    for i in range(len(serializer.data)):
        if movie_pk == serializer.data[i]['pk']:
            idx.append(i)
            break

    xMovie = [data.get('words') for data in serializer.data]
    result = recommend_movies_names(xMovie, idx, serializer)
    final_movie = [get_object_or_404(Movie, pk=i) for i in result]
    final_serializer = UserChoiceSimilarMovieSerializer(final_movie, many=True)
    
    return Response(final_serializer.data)


# 추천 알고리즘
def recommend_movies_names(xMovie, idx, movies):
    
    # 불용어 제거
    countVec = CountVectorizer(max_features=10000, stop_words='english')

    # 영화 키워드 벡터라이징
    dataVectors = countVec.fit_transform(xMovie).toarray()

    # 코사인 유사도
    similarity = cosine_similarity(dataVectors)
    
    # 유사도 내림차순 5개 영화의 인덱스
    idx_collection = []
    for i in idx:
        distances = similarity[i]
        listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
        idx_collection.extend(listofMovies)
 
    # 인덱스를 pk로 바꾸기
    pk_collection = []
    for idx in idx_collection:
        pk_collection.append(movies.data[idx[0]]['pk'])

    return pk_collection


# 검색 알고리즘
# > 편집거리 알고리즘

def serach(lst, keyword):
    fetch_data = []
    for data in lst:
        tmp = {'pk': 0, 'title': '', 'poster_path':'', 'similarity':''}
        tmp['pk'] = data['pk']; tmp['title'] = data['title']; tmp['poster_path'] = data['poster_path']
        tmp['similarity'] = jaro_winkler_similarity(keyword, data['title'])
        fetch_data.append(tmp)
    fetch_data.sort(key=lambda x : -x['similarity'])
    return fetch_data