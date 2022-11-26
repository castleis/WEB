from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Movie, Review
from journal.models import Journal
from accounts.models import Profile
from .serializers import MovieSerializer, ReviewSerializer, ReviewListSerializer,MovieListSerializer

from fuzzywuzzy import fuzz, process
from heapq import heappush
from datetime import date,timedelta

######################################################################################################
# Movie

# 영화 전체 가져오기
@api_view(['GET'])
def get_movie(request):
    movies = get_list_or_404(Movie)
    return Response(MovieSerializer(movies, many=True).data)

# 실시간 검색
@api_view(['GET'])
def search(request):
    ################# 실시간 검색 용도 #################
    target = request.GET.get('search_word').replace(' ','')
    # if user.adult == False:
    # movies = Movie.objects.filter(adult=user.adult)
    movies = get_list_or_404(Movie)     # type: list
    search_movies = []
    for movie in movies:
        movie_title = movie.title.replace(' ','')
        if fuzz.token_sort_ratio(target, movie_title) > 40 or fuzz.partial_ratio(target, movie_title) == 100:
            # print(f'== {target} : {movie_title} ==== >>>> {fuzz.token_sort_ratio(target,movie_title)}')
            heappush(search_movies,(-fuzz.partial_ratio(target,movie_title), -movie.popularity, movie)) 
            a, b, c = zip(*search_movies)
    results = c[:10]
    serializer = MovieListSerializer(results, many=True)
    ################################################
    return Response(serializer.data)

# 영화 추천 알고리즘
# 1. 내가 좋아요하는 영화의 장르 -> 장르 데이터가 어떻게 들어오는지 확인 후 수정 필요
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_by_my_genre(request):
    user = request.user
    my_movies = user.like_movies.all()
    my_genres = []
    for movie in my_movies:
        for genre in movie.genres.all():
            my_genres.append(genre.id)
    # print(f'========================= {my_genres} waler;mcalefasdk')
    my_genres = list(set(my_genres))
    # print(f'we;ir================================fjlna {my_genres}')
    my_genres_movies = []
    for genre in my_genres:
        my_genres_movies += Movie.objects.filter(genres=genre)
    # print(my_genres_movies)
    my_genres_movies = sorted(my_genres_movies, key=lambda x: x.popularity)[-10:]
    # print(f'genres : {my_genres_movies}')
    serializer = MovieListSerializer(my_genres_movies, many=True)
    return Response(serializer.data)

# 2. 내가 팔로우하는 사람이 좋아하는 영화 (좋아요 많은 순)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_by_followings(request):
    user = request.user
    # 유저가 팔로우한 사람들(팔로잉)을 불러오기
    followings = user.followings.all()
    followings_movies = []
    # 각각의 팔로잉들이 좋아하는 영화 목록 가져오기
    for following in followings:
        movies = following.like_movies.all()
        followings_movies += movies
    # ~~ 기준으로 정렬하여 상위 10개만 리턴 -> 중복 제거필요
    movies_set = list(set(followings_movies))
    sorted_movies = []
    for movie in movies_set:
        popularity = (followings_movies.count(movie))*15 + (movie.vote_average)*10 + (movie.popularity)*5
        sorted_movies.append((movie, popularity))
    sorted_movies = sorted(sorted_movies, key= lambda x: x[1])[-10:]
    recommend_movies,a = zip(*sorted_movies)
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)

# 3. 평점이 높은 영화 (vote_average로 sort) -> 높은 순으로 10개만 잘라 보냅니닫
@api_view(['GET'])
def recommend_by_vote_averate(request):
    vote_average_movies = Movie.objects.order_by('-popularity')[:10]
    # for movie in vote_average_movies:
        # print(movie.popularity)
    serializer = MovieListSerializer(vote_average_movies, many=True)
    return Response(serializer.data)

# 4. 금주의 HOT : 리뷰, 저널 많이 작성된 순
@api_view(['GET'])
def recommend_by_weekly_hot(request):
    today = date.today()
    weekly_movies = []
    # 매일매일 업데이트한다고 치고 어제 or 오늘 작성된 것만 가져오는게 어떨까
    # 계산이 좀 줄을듯 ^_^
    movies = []
    reviews = Review.objects.filter(created_at__gte=today-timedelta(days=7))
    for review in reviews:
        # print(f'review : {review.content}')
        movie = Movie.objects.get(pk=review.movie_id)
        movies.append(movie)

    journals = Journal.objects.filter(created_at__gte=today-timedelta(days=7))
    for journal in journals:
        movie = Movie.objects.get(pk=journal.movie_id)
        movies.append(movie)

    movies_set = list(set(movies))
    for movie in movies_set:
        popularity = movies.count(movie)
        heappush(weekly_movies, (-popularity, -movie.vote_average, -movie.popularity, movie))
        a, b, c, weekly_hot_movie = zip(*weekly_movies)
    weekly_hot_movie = list(weekly_hot_movie)[:10]
    serializer = MovieListSerializer(weekly_hot_movie, many=True)
    return Response(serializer.data)

# 영화 상세조회
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 영화 좋아요 -> 사용자의 영화 좋아요 등록, 취소 여부만 리턴
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=movie_id)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_like = False
        else:
            movie.like_users.add(request.user)
            is_like = True
        return Response(is_like)

# 사용자가 좋아요 누른 영화 목록
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def my_movie_list(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    movies = user.like_movies.all()
    # for movie in movies:
        # print(movie.title)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

################################################################################################
# Review

# 영화별 리뷰 조회
@api_view(['GET'])
def best_review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    best_reviews = reviews.annotate(like_count=Count('like_user')).order_by('-like_count')[:3]
    # reviews = Review.objects.raw(f'select * from (select * from movies_review where movie_id=movie) as s1 union all (select * from select review_id, count(*) as review_count from movies_review_like_user group by review_id) as s2 ')
    serializer = ReviewListSerializer(best_reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    # reviews = Review.objects.raw(f'select * from (select * from movies_review where movie_id=movie) as s1 union all (select * from select review_id, count(*) as review_count from movies_review_like_user group by review_id) as s2 ')
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

# 영화 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    user = get_user_model().objects.get(pk=request.user.id)
    profile = Profile.objects.get(user_id=user.id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        movie = get_object_or_404(Movie, pk=movie_id)
        profile.ranking += 20
        profile.save()
        ################## 별점 계산 과정 ##################
        # 이전 values
        pre_vote_average = movie.vote_average
        pre_vote_count = movie.vote_count
        new_vote_point = pre_vote_average * pre_vote_count + float(request.data.get('rank'))
        # 계산 이후 values
        movie.vote_count += 1
        movie.vote_average = round(new_vote_point / movie.vote_count,2)
        movie.save()
        #################################################

        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 삭제, 수정
@api_view(['DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def review_detail(request, review_id):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)
        user = Profile.objects.get(user_id=review.user_id)
        if request.method == 'DELETE':
            # 별점은 소듕한 데이터니까 삭제해도 남겨두도록 하겠읍니다.
            user.ranking -= 20
            user.save()
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                movie = get_object_or_404(Movie, pk=request.data.get('movie'))

                ################## 별점 수정 과정 ##################
                # 이전 values / vote_count는 변하지 않음
                pre_rank = review.rank
                pre_vote_average = movie.vote_average
                movie.vote_average = (pre_vote_average * movie.vote_count) + float(request.data.get('rank') - pre_rank)
                movie.save()
                #################################################

                serializer.save()
                return Response(serializer.data)

# 리뷰 좋아요 -> 사용자의 좋아요 등록, 취소 여부만 return
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_like(request, review_id):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, id=review_id)
        user = get_user_model().objects.get(pk=request.user.id)
        profile = Profile.objects.get(user_id=user.pk)
        if review.like_user.filter(id=request.user.id).exists():
            review.like_user.remove(request.user)
            profile.ranking -= 30
            # is_like는 front에서 실시간으로 숫자 증감을 보여주는데 사용
            is_like = False
        else:
            review.like_user.add(user)
            # print(review.like_user)
            profile.ranking += 30
            is_like = True
        profile.save()
        return Response(is_like)


################################################################################
''' TMDB 영화 요청
def get_movie(request):
    api_key = '919971eefd69cc44b0a9340c46959be3'
    for i in range(1,51):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&region=KR&page={i}'
        response = requests.get(URL).json()
        a = response.get('results')
        for data in a:
            movie = Movie(
                title = data['title'],
                original_title = data['original_title'],
                overview = data['overview'],
                release_date = data['release_date'],
                poster_path = data['poster_path'],
                genre_id = json.dumps(data['genre_ids']),
                popularity = data['popularity'],
                vote_average = data['vote_average'],
                vote_count = data['vote_count'],
                adult = data['adult'],
            )
            movie.save()
    return
'''
''' 영화 좋아요 소스 코드
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)
'''            