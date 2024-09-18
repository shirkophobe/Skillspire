from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

]