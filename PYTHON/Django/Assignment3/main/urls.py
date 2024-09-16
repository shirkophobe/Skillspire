from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display-name/<str:name>', views.displayname, name='display-name'),
    path('display-food/<str:food>', views.displayfood, name='display-food'),
    path('display-vacation/<str:vacation>', views.displayvacation, name='display-vacation')
]
  