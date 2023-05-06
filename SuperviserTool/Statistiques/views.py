from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from .tools import *
from django.http import JsonResponse, HttpResponse
from SuperviserTool.config import qs_app_list
from Supervision.models import HostList
from json import *

def home(request):
    username = None
    qs_host_list = HostList.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    return render(request,'Statistiques/home.html',{'app_list':qs_app_list,'host_list':qs_host_list})

@api_view(['GET'])
def get_memory_usage(request):
    o_memory = MemoryUse.objects.all()
    serialize = GetMemoryDataSerializer(o_memory,many=True)
    json = create_json_data(serialize.data,"memory")

    return JsonResponse(json,safe=False)

@api_view(['GET'])
def get_swap_usage(request):
    o_swap = SwapUse.objects.all()
    serialize = GetSwapDataSerializer(o_swap,many=True)
    json = create_json_data(serialize.data,"swap")
    
    return JsonResponse(json,safe=False)
