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
        obj_app.save()
    except Exception as e:
        print(e)

def add_new_jmx(dict):
    #Conversion du dict en json
    json_data=json.loads(dict)
    #Attribution des variables
    jmx_name = json_data["name"]
    jmx_path_scenario = json_data["path_scenario"]
    jmx_file_resultat = json_data["path_resu"]

    #Ajout dans la base
    try:
        obj_jmx = JmeterJmx()
        obj_jmx.j_name = jmx_name
        if jmx_path_scenario != obj_jmx.j_scenario_path:
            obj_jmx.j_scenario_path = jmx_path_scenario
        obj_jmx.j_resultat_file=jmx_file_resultat
        obj_jmx.save()
    except Exception as e:
        print(e)

def add_new_os(dict):
    json_data=json.loads(dict)

    os = json_data["OS"]
    version = json_data["version"]

    try:
        obj_os = OS()
        obj_os.o_name = os
        obj_os.o_version = version
        obj_os.save()
    except Exception as e:
        print(e)

def add_new_server(dict):
    json_data=json.loads(dict)

    server = json_data["Server"]
    version = json_data["Version"]

    try:
        obj_server = TypeServer()
        obj_server.t_name = server
        obj_server.t_version_server = version
        obj_server.save()
    except Exception as e:
        print(e)