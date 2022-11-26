from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.TextField()
class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField(null=True)
    genres = models.ManyToManyField(Genre, related_name='genre_names')
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    adult = models.BooleanField()
    runtime = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Review(models.Model):
    #FK : 작성 유저, 영화
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # input values : 컨텐트, 별점
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    # 좋아요
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)