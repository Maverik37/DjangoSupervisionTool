from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import *
from SuperviserTool.config import qs_app_list

def home(request):
	qs_host_list = HostList.objects.all()
	qs_app_sup = Application.objects.all()
	username = None
	if request.user.is_authenticated:
		username = request.user.username
	return render(request,'Supervision/home.html',{'app_list':qs_app_list, 'host_list':qs_host_list,'app_sup':qs_app_sup,'connecteduser':username})