from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:user_id>', views.show, name='show'),
    path('<int:user_id>/edit', views.edit, name='edit'),
    path('users/<int:user_id>/destroy', views.destroy, name='destroy'), 
]
