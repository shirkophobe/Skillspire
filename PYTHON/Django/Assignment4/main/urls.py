from django.urls import path
from . import views

urlpatterns = [
    path('display-info/', views.display_info, name='display_info'),
]
