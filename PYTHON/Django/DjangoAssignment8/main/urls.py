from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('destroy/<int:course_id>/', views.confirm_delete, name='confirm_delete'), 
]