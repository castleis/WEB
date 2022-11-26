from rest_framework import serializers
from .models import Journal, JournalComment
from accounts.models import User,Profile
from movies.models import Movie

# 유저가 작성한 모든 저널 조회에 사용
class JournalListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = Journal
        fields = ('id','title','nickname','user')
    
    def get_nickname(self, journal):
        person = User.objects.get(username=journal.user.username)
        person_profile = Profile.objects.get(user_id=person.id)
        return person_profile.nickname

# 저널에 작성된 모든 댓글 조회에 사용
class JournalCommentListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = JournalComment
        fields = ('id','user','nickname','content','created_at', 'comment_like_user')

    def get_nickname(self, journal):
        person = User.objects.get(username=journal.user.username)
        person_profile = Profile.objects.get(user_id=person.id)
        return person_profile.nickname

# 저널에 작성된 댓글 : 생성,수정에 사용
class JournalCommentSerializer(serializers.ModelSerializer):
    # journal_recomment = serializers.
    class Meta:
        model = JournalComment
        fields = '__all__'
        read_only_fields = ('user','journal','parent', 'comment_like_user')
    
    # def get_recomment(self,instance):
    #     response = super().get_recomment(instance)
    #     response['parent']
    #     pass

# Journal 디테일 조회 
class JournalSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    movie_title = serializers.SerializerMethodField()
    class Meta:
        model = Journal
        fields = "__all__"
        read_only_fields = ('user','like_user', 'nickname')

    def get_nickname(self, journal):
        person = User.objects.get(username=journal.user.username)
        person_profile = Profile.objects.get(user_id=person.id)
        return person_profile.nickname
    
    def get_movie_title(self, journal):
        movie = Movie.objects.get(pk=journal.movie_id)
        return movie.title