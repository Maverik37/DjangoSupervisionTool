from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .tool import *
from SuperviserTool.config import qs_app_list

def home(request):
	qs_host_list = HostList.objects.all()
	qs_app_sup = Application.objects.all()
	username = None
	if request.user.is_authenticated:
		username = request.user.username
	return render(request,'Supervision/home.html',{'app_list':qs_app_list, 'host_list':qs_host_list,'app_sup':qs_app_sup,'connecteduser':username})

@login_required
def add_host_supervision_page(request):
	qs_os_list= OS.objects.all()
	qs_server_list= TypeServer.objects.all()
	print(request.body)
	if request.user.is_authenticated:
		username = request.user.username
	return render(request,'Supervision/ajout_machine_supervision.html',{'app_list':qs_app_list,'connecteduser':username,"os_list":qs_os_list,"server_list":qs_server_list})

@login_required
@csrf_exempt
def add_host_bdd(request):
	if request.method == "POST":
		try:
			add_new_host(request.body)
			return HttpResponse("Machine ajoutée",status=200)
		except Exception as e:
			return HttpResponse(e,status=500)