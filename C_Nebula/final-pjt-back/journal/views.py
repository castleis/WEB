from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.db.models import Count
# rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Models
from .models import Journal, JournalComment
from accounts.models import Profile
from. serializers import JournalSerializer, JournalListSerializer, JournalCommentSerializer, JournalCommentListSerializer
################################################################################################
# 전체유저가 작성한 저널 리스트 조회
@api_view(['GET'])
def journal_list(request):
    # num = request.data.order
    num = request.GET.get('order')
    num = int(num)
    # print(request.GET.get['order'])
    # sorting = {0:'-id', 1:'id', 2: 'like_count'}
    journals = Journal.objects.filter(private=False)
    # for journal in journals:
    #     print(journal.journalcomment_set.all())
    my_journals = Journal.objects.filter(user=request.user, private=True)
    if num == 0:
        journals = (journals | my_journals).order_by('-id')
        # print(journals)
    elif num == 1:
        journals = (journals | my_journals).order_by('id')
        # print(journals)
    elif num == 2:
        journals = (journals | my_journals).annotate(like_count=Count('like_user')*3+ Count('journalcomment')*2).order_by('-like_count')
        # print(journals)
    serializer = JournalListSerializer(journals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def profile(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    if request.method == 'GET':
        journals = Journal.objects.filter(user=user)
        serializer = JournalListSerializer(journals, many=True)
        return Response(serializer.data)

# 저널 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def journal_create(request):
    profile = Profile.objects.get(user=request.user.pk)
    serializer = JournalSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        profile.ranking += 20
        profile.save()
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# GET: 저널 디테일, DELETE: 저널 삭제, PUT: 저널 수정
@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def journal_detail(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)

    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        user = Profile.objects.get(pk=request.user.pk)
        user.ranking -= 20
        user.save()
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def journal_like(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    user = get_user_model().objects.get(pk=journal.user_id)
    profile = Profile.objects.get(user_id=user.id)
    if journal.like_user.filter(pk=request.user.pk).exists():
        journal.like_user.remove(request.user)
        profile.ranking -= 30
        is_like = False
    else:
        journal.like_user.add(request.user)
        profile.ranking += 30
        is_like = True
    profile.save()
    return Response(is_like)
    
################################################################################################
# Comments
# 저널의 댓글 조회하기
@api_view(['GET'])
def journal_comments(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    # 역참조 이름이 이게 맞나?????
    comments = journal.journalcomment_set.all().filter(parent__isnull=True).order_by('-id')
    serializer = JournalCommentListSerializer(comments, many=True)
    return Response(serializer.data)

# 저널에 댓글 작성하기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def journal_comments_create(request,journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    user = get_user_model().objects.get(id=journal.user.id)
    profile = Profile.objects.get(user=user.id)
    serializer = JournalCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        profile.ranking += 10
        profile.save()
        serializer.save(journal=journal, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def journal_comments_detail(request, comment_id):
    comment = get_object_or_404(JournalComment, id=comment_id)
    user = get_user_model().objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user.id)
    if request.method == 'DELETE':
        profile.ranking -= 10
        profile.save()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == 'PUT':
        serializer = JournalCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comments_like(request, comment_id):
    comment = get_object_or_404(JournalComment, id=comment_id)
    user = Profile.objects.get(user_id=comment.user_id)
    if comment.comment_like_user.filter(id=request.user.pk).exists():
        comment.comment_like_user.remove(request.user)
        user.ranking -= 30
        is_comment_like = False
    else:
        comment.comment_like_user.add(request.user) 
        user.ranking += 30
        is_comment_like = True
    user.save()
    return Response(is_comment_like)

# 대댓글~!!!!
@api_view(['GET'])
def journal_recomments(request, journal_id, comment_id):
    journal = get_object_or_404(Journal, id=journal_id)
    comment = get_object_or_404(JournalComment, id=comment_id)
    # 역참조 이름 확인 필필필!!!!!!!!!!
    recomments = journal.journalcomment_set.filter(parent=comment).order_by('-id')
    serializer = JournalCommentListSerializer(recomments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def journal_recomments_create(request, journal_id, comment_id):
    journal = get_object_or_404(Journal, id=journal_id)
    parent_comment = get_object_or_404(JournalComment, id=comment_id)
    user = get_user_model().objects.get(id=request.user.id)
    serializer = JournalCommentSerializer(data=request.data)
    profile = Profile.objects.get(user_id=user.id)
    if serializer.is_valid(raise_exception=True):
        profile.ranking += 10
        profile.save()
        serializer.save(journal=journal, user=request.user, parent=parent_comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response('failed')