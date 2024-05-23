from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


User = get_user_model()

# 유저가 좋아하는 영화, 유저에 대한 정보 제공
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

