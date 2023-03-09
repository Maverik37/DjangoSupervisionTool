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


def add_new_app(dict):
    #Conversion du dict en json
    json_data=json.loads(dict)
    #Attribution des variables
    app_name = json_data["Application"]
    host_id = json_data["hostname"].split('-')[0] #On prend que l'id pour récupérer l'objet en base
    jmx_id = json_data["JMX"].split('-')[0] #On prend que l'id pour récupérer l'objet en base

    #on récup les objets pour assurer l'ajout en base après
    qs_host = HostList.objects.get(id=host_id)
    print(qs_host)
    qs_jmx = JmeterJmx.objects.get(id=jmx_id)
    print(qs_jmx)

    #On ajoute la nouvelle application dans la base
    try:
        obj_app=Application()
        obj_app.a_name = app_name
        obj_app.a_host = qs_host
        obj_app.a_scenario_jmx = qs_jmx
        obj_app.a_precedent_state = "OK"
        obj_app.a_actual_state = "OK"
        obj_app.save()
    except Exception as e:
        print(e)