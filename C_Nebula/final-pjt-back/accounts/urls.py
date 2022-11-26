from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    # 팔로우
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/following/list/', views.following_list),
    path('<int:user_pk>/follower/list/', views.follower_list),
    # 프로필
    path('user_ranking/', views.user_ranking),
    path('<int:user_id>/', views.profile),
    path('create/', views.profile_create),
    path('detail/', views.profile_update),
    # 회원탈퇴
    path('delete_user/', views.delete_user),
]
