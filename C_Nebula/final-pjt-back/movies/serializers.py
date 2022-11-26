from rest_framework import serializers
from .models import Movie, Review, Genre
from accounts.models import Profile,User
from django.contrib.auth import get_user_model
# 영화 목록 
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'id')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'id')

# 영화 디테일  
class MovieSerializer(serializers.ModelSerializer):
    genre_names = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'

    def get_genre_names(self, genres):
        genrename = Genre.objects.filter(genre_names=genres)
        return GenreSerializer(genrename, many=True).data

# 리뷰 조회에 사용
class ReviewListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ('id', 'content', 'rank', 'user', 'like_user', 'nickname')

    def get_nickname(self, review):
        person = User.objects.get(username=review.user.username)
        person_profile = Profile.objects.get(user_id=person.pk)
        return person_profile.nickname

# 리뷰 디테일 -> create에 사용
class ReviewSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user','movie','like_user','nickname')

    def get_nickname(self, review):
        person = User.objects.get(username=review.user.username)
        person_profile = Profile.objects.get(user_id=person.pk)
        return person_profile.nickname
