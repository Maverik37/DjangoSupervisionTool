#!/bin/env  python3.6
import os
import sys
import django
import subprocess, re
#Configuration pour pouvoir importer les modèles django
sys.path.append('/home/fourbasse/scripts/DJANGO/DjangoSupervisionTool/DjangoSupervisionTool/SuperviserTool/')
os.environ["DJANGO_SETTINGS_MODULE"] = "SuperviserTool.settings"
django.setup()

#Import du modèle
from Supervision.models import *

qs_scenarios_list=JmeterJmx.objects.all()

for scenario in qs_scenarios_list:
    