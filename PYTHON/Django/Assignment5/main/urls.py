from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtwo/', views.addtwo, name='addtwo'),
    path('reset/', views.reset, name='reset'),
]
