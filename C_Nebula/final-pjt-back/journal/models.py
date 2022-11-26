from django.db import models
from django.conf import settings
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Journal(models.Model):
    # FK : 작성 유저, 영화
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    # 저널 좋아요
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_journals')
    
    # input values : 제목, 내용, 별점, 공개범위(기본값 False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    private = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class JournalComment(models.Model):
    # FK : 작성 유저, 저널, 부모 댓글
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='journal_recomment', null=True) 
    
    # 댓글 좋아요
    comment_like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_like_journal_comments')
    
    # input value : 내용
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)