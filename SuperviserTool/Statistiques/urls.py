from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
app_name = 'Statistiques'

urlpatterns= [
	path('', views.home, name="statistiques_index"),
    path('api/get_memory_data',views.get_memory_usage, name="get_memory_usage"),
    path('api/get_swap_data',views.get_swap_usage, name="get_swap_usage"),
]