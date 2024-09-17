from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtwo/', views.add_two, name='add_two'),
    path('reset/', views.reset, name='reset'),
]
