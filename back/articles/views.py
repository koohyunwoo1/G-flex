from django.shortcuts import render, get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article,Comment

from .serializers import CommentSerializer, ArticleSerializer, ArticleListSerializer



# 자유게시판 전체 글 조회, 글 작성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_show_create(request):

    if request.method == 'GET':

        articles = get_list_or_404(Article)

        serializer = ArticleListSerializer(articles, many= True)

        return  Response(serializer.data)
    
    elif request.method == 'POST':

        serializer = ArticleListSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 특정 게시물 들어가기, 수정하기, 삭제
@api_view(['GET', 'PUT', 'DELETE'])    
def article_detail_update_delete(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':

        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        if request.user == article.user:
            # 수정을 요구한 유저와 글을 작성한 유저가 같다면?

            serializer = ArticleSerializer(instance=article, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
    elif request.method == 'DELETE':

        if request.user == article.user:

            article.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

# 게시물에 들어가서 댓글 생성하기
@api_view(['GET','POST'])
def create_comment(request, article_pk):

    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comments.all()

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user= request.user
        article = get_object_or_404(Article, pk=article_pk)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)

            comments = article.comments.all()
            serializer = CommentSerializer(comments,many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 게시물에 들어가서 댓글 수정, 삭제하기
@api_view(['PUT', 'DELETE'])
def create_update_delete(request, article_pk, comment_pk):

    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':

        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    
    elif request.method == 'DELETE':

        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
