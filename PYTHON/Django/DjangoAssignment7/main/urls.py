from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_user, name='create_user'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),  
]
