from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Applications.urls')),
    path('supervision/',include('Supervision.urls')),
]
