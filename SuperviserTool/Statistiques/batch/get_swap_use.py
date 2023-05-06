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

#Import des tables
from Supervision.models import HostList
from Statistiques.models import SwapUse

#Import de quelques fonctions utiles
from batch_tools import *

o_localhost = HostList.objects.get(h_name="localhost")

f_swap_use = convert_byte_to_float(psutil.swap_memory().used)
f_swap_free = convert_byte_to_float(psutil.swap_memory().free)
current_date = current_date_to_string()

try:
    o_swap = SwapUse()
    o_swap.s_host = o_localhost
    o_swap.s_datetime = current_date
    o_swap.s_free_memory = f_swap_free
    o_swap.s_used_memory = f_swap_use
    o_swap.save()
except Exception as e :
    print(e)