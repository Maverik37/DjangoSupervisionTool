#!/bin/env  python3
import os
import sys
import django
import subprocess, re, psutil, datetime
from datetime import *
#Configuration pour pouvoir importer les modèles django
sys.path.append('/home/fourbasse/scripts/DJANGO/DjangoSupervisionTool/DjangoSupervisionTool/SuperviserTool/')
os.environ["DJANGO_SETTINGS_MODULE"] = "SuperviserTool.settings"
django.setup()

#Import des modèles nécessaires
from Supervision.models import HostList
from Statistiques.models import MemoryUse
#Import fichier tools
from batch_tools import *

# On va récupérer la machine localhost pour le moment
o_localhost = HostList.objects.get(h_name="localhost")

f_mem_used = convert_byte_to_float(psutil.virtual_memory().used)
f_mem_free = convert_byte_to_float(psutil.virtual_memory().free)
current_date = current_date_to_string()

#Ajout dans la base 
try:
    o_memory = MemoryUse()
    o_memory.m_host = o_localhost
    o_memory.m_datetime = current_date
    o_memory.m_free_memory = f_mem_free
    o_memory.m_used_memory = f_mem_used
    o_memory.save()
except Exception as e:
    print(e)
