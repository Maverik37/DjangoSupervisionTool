from .models import *
from Supervision.models import HostList

def create_json_data(queryset,type):
    #On va récupérer la liste des machines
    if type == "memory":
        host_id = []
        data = {}
        for key in queryset:
            if key.get('m_host') not in host_id:
                host_id.append(key.get('m_host'))
        for host in host_id:
            hostname = HostList.objects.get(id= host)
            data[hostname.h_name]={}
            data[hostname.h_name]["labels"]=[]
            data[hostname.h_name]["mem_total"]= hostname.h_total_memory
            data[hostname.h_name]["mem_free_data"]=[]
            data[hostname.h_name]["mem_used_data"]=[]
            for d in queryset:
                # regrouper selon le type de données
                if d["m_datetime"] not in data[hostname.h_name]["labels"]:
                    data[hostname.h_name]["labels"].append(d["m_datetime"]) 
                data[hostname.h_name]["mem_free_data"].append(d["m_free_memory"])
                data[hostname.h_name]["mem_used_data"].append(d["m_used_memory"]) 
        return data            
    elif type == "swap":
        host_id = []
        data = {}
        print(queryset)
        for key in queryset:
            if key.get('s_host') not in host_id:
                host_id.append(key.get('s_host'))
        for host in host_id:
            hostname = HostList.objects.get(id= host)
            data[hostname.h_name]={}
            data[hostname.h_name]["labels"]=[]
            data[hostname.h_name]["swap_total"]= hostname.h_total_swap
            data[hostname.h_name]["swap_free_data"]=[]
            data[hostname.h_name]["swap_used_data"]=[]
            
            for d in queryset:
                if d["s_datetime"] not in data[hostname.h_name]["labels"]:
                    data[hostname.h_name]["labels"].append(d["s_datetime"])
                data[hostname.h_name]["swap_free_data"].append(d["s_free_memory"])
                data[hostname.h_name]["swap_used_data"].append(d["s_used_memory"])
        return data
    