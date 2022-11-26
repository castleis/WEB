from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    adult = models.BooleanField(null=True)
    ranking = models.IntegerField(default=0)
    nickname = models.CharField(max_length=10)