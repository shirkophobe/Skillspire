from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('main.urls')),
    path('admin/', admin.site.urls),
]
