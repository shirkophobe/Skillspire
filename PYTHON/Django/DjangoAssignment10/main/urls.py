from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('news_feed/', views.news_feed, name='news_feed'),
    path('login/', views.user_login, name='login'),  
]
