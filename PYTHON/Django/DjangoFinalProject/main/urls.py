from django.urls import path
from . import views

urlpatterns = [
    # path('', views.news_feed, name='home'),  
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('news_feed/', views.news_feed, name='news_feed'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
