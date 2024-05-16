from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_show_create, name='article_show_create'),
    path('<int:article_pk>/', views.article_detail_update_delete, name='article_detail_update_delete'),
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.create_update_delete, name='create_update_delete'),
    
]
