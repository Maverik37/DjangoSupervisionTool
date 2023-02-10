from django.urls import path
from . import views

app_name = 'Applications'

urlpatterns= [
	path('',views.home, name="app_index"),
]
