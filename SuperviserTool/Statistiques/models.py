from django.db import models
from Supervision.models import HostList

class MemoryUse(models.Model):
    m_host = models.ForeignKey(HostList,verbose_name="Machine",on_delete=models.CASCADE,blank=True,null=True)
    m_datetime = models.CharField(max_length=100, verbose_name="Date", blank=True, null=True)
    m_free_memory = models.FloatField(max_length=40, verbose_name="Mémoire Libre", blank=True,null=True)
    m_used_memory = models.FloatField(max_length=40, verbose_name="Mémoire utilisée", blank=True,null=True)

    def __str__(self):
        return str(self.id)+"_"+self.m_host.h_name

class SwapUse(models.Model):
    s_host = models.ForeignKey(HostList,verbose_name="Machine",on_delete=models.CASCADE,blank=True,null=True)
    s_datetime = models.CharField(max_length=100, verbose_name="Date", blank=True, null=True)
    s_free_memory = models.FloatField(max_length=40, verbose_name="Mémoire Libre", blank=True,null=True)
    s_used_memory = models.FloatField(max_length=40, verbose_name="Mémoire utilisée", blank=True,null=True)

    def __str__(self):
        return str(self.id)+"_"+self.s_host.h_name