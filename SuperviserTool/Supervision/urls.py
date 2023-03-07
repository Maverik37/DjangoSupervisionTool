from django.urls import path
from . import views

app_name = 'Supervision'

urlpatterns= [
	path('',views.home, name="supervision_index"),
    path('addhostform/',views.add_host_supervision_page, name="supervision_add_host_page"),
    path('add_host_bdd/',views.add_host_bdd, name="add_host_bdd"),
]
