from django.urls import path
from . import views

app_name = 'Supervision'

urlpatterns= [
	path('',views.home, name="supervision_index"),
    path('addhost/',views.add_host_supervision, name="supervision_add_host"),
]
