from django.db import models

class OS(models.Model):
    o_name = models.CharField(default="Unknown", max_length=100,verbose_name="Nom",unique=True,blank=True,null=True)
    o_version = models.CharField(default="NA", max_length=10,verbose_name="Version OS",blank=True,null=True)

    def __str__(self):
        return self.o_name+" v"+self.o_version

class TypeServer(models.Model):
    t_name = models.CharField(default="Unknown", max_length=100, verbose_name="Nom", unique=True, blank=True,null=True)
    t_version_server = models.CharField(default="NA", max_length=10,verbose_name="Version Serveur",blank=True,null=True)

    def __str__(self):
        return self.t_name+" v"+self.t_version_server

class HostList(models.Model):
    h_name = models.CharField(max_length=50, verbose_name="Nom")
    h_ip = models.CharField(max_length=50, verbose_name="IP")
    h_os = models.ForeignKey(OS,related_name="o_os_installed",verbose_name="OS", on_delete=models.CASCADE,blank=True,null=True)
    h_type_server = models.ForeignKey(TypeServer,related_name="t_server_installed", verbose_name="Serveur", on_delete=models.CASCADE,blank=True,null=True)
    h_status = models.CharField(max_length=10,verbose_name="Etat")

    def __str__(self):
        return self.h_name+"_"+self.h_ip + "_" + self.h_status


class JmeterJmx(models.Model):
    j_name = models.CharField(max_length=100, verbose_name="Nom")
    j_scenario_path= models.CharField(max_length=200,default="/home/fourbasse/scripts/JMETER/scenarios/", verbose_name="Path")
    j_resultat_file = models.CharField(max_length=200,default="/home/fourbasse/scripts/JMETER/resultats/", verbose_name="Fichier")

    def __str__(self):
        return self.j_name+"_"+self.j_scenario_path+"_"+self.j_resultat_file

class Application(models.Model):
    a_name = models.CharField(max_length=200,verbose_name="Nom",unique=True)
    a_host = models.ForeignKey(HostList,related_name="h_machine",on_delete=models.CASCADE,blank=True,null=True)
    a_scenario_jmx = models.ForeignKey(JmeterJmx,related_name="j_jmx",on_delete=models.CASCADE,blank=True,null=True)
    a_precedent_state = models.CharField(max_length=10,verbose_name="Etat précédent")
    a_actual_state = models.CharField(max_length=10,verbose_name="Etat actuel")

    def __str__(self):
        return self.a_name+"-"+self.a_actual_state

