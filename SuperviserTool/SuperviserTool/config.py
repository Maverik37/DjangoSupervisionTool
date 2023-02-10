from Applications.models import *

qs_app_list = DjangoApplication.objects.all().order_by('id')

obj_app_list= {}

for app in qs_app_list:
    obj_app_list[app.d_name]={}
    obj_app_list[app.d_name]["portail_name"] = app.d_portail_name
    obj_app_list[app.d_name]["url"] = app.d_name+":"+app.d_url_home
