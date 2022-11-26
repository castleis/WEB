from rest_framework import serializers
# from django.contrib.auth import authenticate
# from django.contrib.auth import get_user_model
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username',)