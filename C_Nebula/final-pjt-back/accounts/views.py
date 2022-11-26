from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .models import Profile

from rest_framework import status
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserListSerializer, ProfileSerializer
# Create your views here.

# FOLLOW
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def follow(request, user_pk):
    user = request.user
    if user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        profile = Profile.objects.get(user=person.id)
        # 로그인된 유저가 아닌 타 유저만 팔로우할 수 있도록
        if user != person:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                profile.ranking -= 30
                followed = False
            else:
                person.followers.add(user)
                profile.ranking += 30
                followed = True
            profile.save()
            # 팔로우 등록/취소 여부만 보냅니닫!
            return Response(followed)
        return Response('user!=person')
    return Response('user_is_not_authenticated')

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def following_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    followings = user.followings.all()
    results = []
    for following in followings:
        # print(following.pk)
        results.append(Profile.objects.get(pk=following.pk))
    serializer = ProfileSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def follower_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    followers = user.followers.all()
    data = []
    for follower in followers:
        data.append(Profile.objects.get(pk=follower.pk))
    serializer = ProfileSerializer(data, many=True)
    return Response(serializer.data)

################################################################################
# PROFILE
@api_view(['GET'])
def profile(request, user_id):
    # user = get_object_or_404(get_user_model(), id=user_id)
    profile = get_object_or_404(Profile, user=user_id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST'])
def profile_create(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
        return Response('우승')

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def profile_update(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    profile = get_object_or_404(Profile, user=user)
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
        return Response(serializer.data)


@api_view(['DELETE'])
def delete_user(request):
    user = get_object_or_404(get_user_model(), id=request.user.pk)
    get_user_model().delete(user)
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_ranking(request):
    profiles = Profile.objects.all().order_by('-ranking')[:3]
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
    

