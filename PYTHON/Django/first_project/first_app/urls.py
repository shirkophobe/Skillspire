from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index),
    # # path('displayinfo', views.displayinfo),
    # # path('displaytime', views.displaytime),
    path('display-name/<name>', views.displayname),
    path('display-food/<food>', views.displayfood),
    path('display-vacation/<vacation>', views.displayvacation)
]
