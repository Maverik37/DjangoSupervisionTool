from django.shortcuts import render
from SuperviserTool.config import obj_app_list
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import *
from Supervision.models import *

def home(request):
	obj_host_ko=HostList.objects.filter(h_status="KO")
	is_host_ko = False
	if obj_host_ko.exists():
		is_host_ko= True

	return render(request,'Applications/base.html',{'app_list':obj_app_list,"is_host_ko":is_host_ko,"list_host_ko":obj_host_ko})