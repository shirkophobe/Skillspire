# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('current_time/', views.current_datetime, name='current_time'),
]
