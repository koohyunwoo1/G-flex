from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [

    path('filter/', views.filter_movies_by_genre_and_mood, name='filter_movies_by_genre_and_mood'),


    # mood
    path('mood/', views.mood_list),
    path('mood/<int:mood_pk>/', views.mood_detail),

    # genre

    path('genre/', views.genre_list),
    path('genre/<int:genre_pk>/', views.genre_detail),

    # movies
    
    path('', views.home, name='home'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/like/', views.like_movie, name='like_movie'),
    path('<int:user_pk>/recommendation/', views.user_like_movie, name='user_like_movie'),
    path('<int:movie_pk>/similar/', views.similar_movie, name='similar_movie'),


    
    path('<str:movie_name>/', views.search_movie, name='search_movie'),

    # 댓글
    path('<int:movie_pk>/comments/', views.create_show_comment, name='create_show_comment'),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.update_delete_comment, name='update_delete_comment'),

]
