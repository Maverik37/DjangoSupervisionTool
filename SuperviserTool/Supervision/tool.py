from .models import *
import json


def add_new_host(dict):
    # On converti en JSON le contenu de la requête 
    json_data=json.loads(dict)

    #On réattribut le contenu dans des variables
    hostname = json_data["hostname"]
    ip = json_data["ip"]

    #on va récup ici l'OS dans la table OS
    os_name = json_data["os"].split('-')[0]
    os_version = json_data["os"].split('-')[1]
    obj_os = OS.objects.get(o_name=os_name, o_version=os_version)

    # Meme chose pour le type de server
    server_name = json_data["server"].split('-')[0]
    server_version = json_data["server"].split('-')[1]
    obj_server = TypeServer.objects.get(t_name=server_name, t_version_server=server_version)

    #on ajoute la nouvelle machine
    try:
        obj_host=HostList()
        obj_host.h_name = hostname
        obj_host.h_ip = ip
        obj_host.h_os = obj_os
        obj_host.h_type_server = obj_server
        obj_host.h_status = "OK"
        obj_host.save()
    except Exception as e:
        print(e)
