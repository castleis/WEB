from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.get_movie, name='get_movie'),
    # 검색
    path('search/', views.search),
    # 추천
    path('recommend/my_genres/', views.recommend_by_my_genre),
    path('recommend/my_followings/', views.recommend_by_followings),
    path('recommend/vote_average/', views.recommend_by_vote_averate),
    path('recommend/weekly_hot/', views.recommend_by_weekly_hot),
    # 영화
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/movie_likes/', views.movie_like),
    path('<int:user_id>/my_movie_list/', views.my_movie_list),
    # 리뷰
    path('<int:movie_id>/review/', views.review_list),
    path('<int:movie_id>/bestreview/', views.best_review_list),

    path('<int:movie_id>/review/create/', views.review_create),
    path('review/<int:review_id>/', views.review_detail),
    path('review/<int:review_id>/review_likes/', views.review_like),
]