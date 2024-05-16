from rest_framework import serializers

from .models import Article,Comment 
from django.contrib.auth import get_user_model

User = get_user_model()


# 댓글

class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    user = UserSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = ('pk', 'content', 'created_at', 'updated_at', 'user')
        read_only_fields = 'article'


# 단일 게시글 조회

class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only = True)

    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'created_at', 'updated_at', 'user')

class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only = True)

    class Meta:
        model = Article
        fields = ('pk', 'title', 'user', 'created_at')