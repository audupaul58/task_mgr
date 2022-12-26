
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('managers.urls')),
    path('auth/', include('authApp.urls')),
]
