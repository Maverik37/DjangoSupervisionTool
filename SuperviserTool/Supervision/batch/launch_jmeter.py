#!/bin/env  python3.6
import os
import sys
import django
import subprocess, re
import pandas as pd
#Configuration pour pouvoir importer les modèles django
sys.path.append('/home/fourbasse/scripts/DJANGO/DjangoSupervisionTool/DjangoSupervisionTool/SuperviserTool/')
os.environ["DJANGO_SETTINGS_MODULE"] = "SuperviserTool.settings"
django.setup()

#Import du modèle
from Supervision.models import *

class JMX():
    #Fonction pour lancer le scenarios jmeter
    def launch_scenarios(path,name,file):
        #on construit la commande à lancer
        jmeter_command = "rm -f "+file+";/home/fourbasse/scripts/JMETER/apache-jmeter-5.5/bin/jmeter -n -t "+path+name
        #Le lancement de la commande est mise dans le try
        try:
            res_command = subprocess.run(jmeter_command,shell=True,stdout=subprocess.PIPE)
        except Exception as e:
            print(e)
    def get_result(file,app_linked):
        csv_data = pd.read_csv(file,header=0)
        nb_rows = len(csv_data.index)
        failed_row=csv_data[csv_data.success== False]
        if nb_rows > 1:
            failed_row=csv_data[csv_data.success== False]
            nb_fail = len(failed_row.index)
            for app in app_linked:
                if nb_fail == 0 :
                    if app.a_actual_state == "OK" and app.a_precedent_state == "KO":
                        try:
                            app.a_precedent_state = "OK"
                            app.save()
                        except Exception as e:
                            print(e)
                    elif app.a_actual_state == "KO" and app.a_precedent_state == "KO":
                        try:
                            app.a_actual_state = "OK"
                            app.save()
                        except Exception as e:
                            print(e)
                    elif app.a_actual_state == "KO" and app.a_precedent_state == "OK":
                        try:
                            app.a_actual_state = "OK"
                            app.save()
                        except Exception as e:
                            print(e)
                else:
                    if app.a_actual_state == "OK" and app.a_precedent_state == "OK":
                        try:
                            app.a_actual_state = "KO"
                            app.save()
                        except Exception as e:
                            print(e)
                    elif app.a_actual_state == "KO" and app.a_precedent_state == "OK":
                        try:
                            app.a_precedent_state = "KO"
                            app.save()
                        except Exception as e:
                            print(e)
                    elif app.a_actual_state == "OK" and app.a_precedent_state == "KO":
                        try:
                            app.a_actual_state = "KO"
                            app.save()
                        except Exception as e:
                            print(e)
        else:
            for index,row in csv_data.iterrows():
                for app in app_linked:
                    # print(app.a_name,app.a_actual_state)
                    if row.success:
                        if app.a_actual_state == "OK" and app.a_precedent_state == "KO":
                            try:
                                app.a_precedent_state = "OK"
                                app.save()
                            except Exception as e:
                                print(e)
                        elif app.a_actual_state == "KO" and app.a_precedent_state == "KO":
                            try:
                                app.a_actual_state = "OK"
                                app.save()
                            except Exception as e:
                                print(e)
                        elif app.a_actual_state == "KO" and app.a_precedent_state == "OK":
                            try:
                                app.a_actual_state = "OK"
                                app.save()
                            except Exception as e:
                                print(e)
                    else:
                        if app.a_actual_state == "OK" and app.a_precedent_state == "OK":
                            try:
                                app.a_actual_state = "KO"
                                app.save()
                            except Exception as e:
                                print(e)
                        elif app.a_actual_state == "KO" and app.a_precedent_state == "OK":
                            try:
                                app.a_precedent_state = "KO"
                                app.save()
                            except Exception as e:
                                print(e)
                        elif app.a_actual_state == "OK" and app.a_precedent_state == "KO":
                            try:
                                app.a_actual_state = "KO"
                                app.save()
                            except Exception as e:
                                print(e)

#Main du script

if __name__ == "__main__":
    # On récupére la liste des scénarios jmeter
    qs_scenarios_list=JmeterJmx.objects.all()

    #on parcourt cette liste
    for scenario in qs_scenarios_list:
        #On attribue des variables pour chaque champs
        scenario_name = scenario.j_name
        scenario_path = scenario.j_scenario_path
        scenario_res = scenario.j_resultat_file
        
        #on appelle la classe JMX pour lancer les scenarios
        try:
            JMX.launch_scenarios(scenario_path,scenario_name,scenario_res)
        except:
            print("Erreur dans le lancement du scenario",scenario_name)

        #on appelle la classe JMX pour le fichier résultat
        try:
            qs_app_linked = Application.objects.filter(a_scenario_jmx=scenario)
            JMX.get_result(scenario_res,qs_app_linked)
        except Exception as e:
            print("Erreur la lecture",scenario_res)
            print(e)

