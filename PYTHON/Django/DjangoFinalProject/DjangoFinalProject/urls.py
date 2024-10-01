from django.contrib import admin
from django.urls import path, include
from main import views  

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),  # Now it correctly references your app's views
]
