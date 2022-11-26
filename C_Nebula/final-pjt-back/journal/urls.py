from django.urls import path
from . import views

app_name='journal'
urlpatterns = [
    # journal
    path('', views.journal_list),
    path('create/', views.journal_create),
    path('<int:journal_id>/detail/', views.journal_detail),
    path('<int:journal_id>/journal_likes/', views.journal_like),
    # profile
    path('<int:user_id>/profile/', views.profile),
    # comments
    path('<int:journal_id>/comments/', views.journal_comments),
    path('<int:journal_id>/comments/create/', views.journal_comments_create),
    path('<int:comment_id>/comments/detail/', views.journal_comments_detail),
    path('<int:comment_id>/comments_likes/', views.comments_like),
    # recomments
    path('<int:journal_id>/<int:comment_id>/recomments/', views.journal_recomments),
    path('<int:journal_id>/<int:comment_id>/recomments/create/', views.journal_recomments_create)

]
