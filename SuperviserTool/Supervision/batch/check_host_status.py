#!/bin/env  python3.9
import os
import sys
import django
import subprocess, re
#Configuration pour pouvoir importer les modèles django
sys.path.append('/home/fourbasse/scripts/DJANGO/DjangoSupervisionTool/DjangoSupervisionTool/SuperviserTool/')
os.environ["DJANGO_SETTINGS_MODULE"] = "SuperviserTool.settings"
django.setup()

#Import du modèle
from Supervision.models import HostList

qs_list_machine = HostList.objects.all().order_by('id')

for host in qs_list_machine:
    s_host_name = host.h_name
    s_prec_host_status = host.h_status
    shell_command = "cd /home/fourbasse/Vagrant ; vagrant status "+s_host_name+ "| grep "+s_host_name+" | awk '{print $2}'"

    res_command = subprocess.run(shell_command,shell=True,stdout=subprocess.PIPE)
    host_status_act= "OK" if (re.search("running",res_command.stdout.decode('UTF-8'))) else "KO"

    #On va vérifier l'état de la machine en base
    if host_status_act != s_prec_host_status:
        host.h_status = host_status_act
        host.save()
    

    

