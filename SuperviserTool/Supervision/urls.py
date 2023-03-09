from django.urls import path
from . import views

app_name = 'Supervision'

urlpatterns= [
	path('',views.home, name="supervision_index"),
    path('addhostform/',views.add_host_supervision_page, name="supervision_add_host_page"),
    path('add_host_bdd/',views.add_host_bdd, name="add_host_bdd"),
    path('addappform/',views.add_app_supervision_page, name="supervision_add_app_page"),
    path('add_app_bdd/',views.add_app_bdd, name="add_app_bdd"),
    path('add_jmx_bdd/',views.add_jmx_bdd, name="add_jmx_bdd"),
    path('add_os_bdd/',views.add_os_bdd, name="add_os_bdd"),
    path('add_server_bdd/',views.add_server_bdd, name="add_server_bdd"),
]
