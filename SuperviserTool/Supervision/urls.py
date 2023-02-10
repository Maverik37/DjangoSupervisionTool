from django.urls import path
from . import views

app_name = 'Supervision'

urlpatterns= [
	path('',views.home, name="supervision_index"),
]
