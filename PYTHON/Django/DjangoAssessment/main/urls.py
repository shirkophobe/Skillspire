from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'), #Part 1
    path('about/', views.about, name='about'), #Part 1
    path('greet/<str:name>/', views.greet, name='greet'),  # Part 2
    path('contact/', views.contact, name='contact'), #Part 3
    path('submit_contact/', views.submit_contact, name='submit_contact'), #Part 3
]