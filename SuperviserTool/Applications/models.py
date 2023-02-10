from django.db import models

class DjangoApplication(models.Model):
    d_name = models.CharField(max_length=100,verbose_name="Application")
    d_portail_name = models.CharField(max_length=100,verbose_name="Ref Portail")
    d_views = models.CharField(max_length=100,verbose_name="views")
    d_url_home= models.CharField(max_length=300,verbose_name="URL")

    def __str__(self):
        return self.d_name+" "+self.d_portail_name+" "+self.d_views+" "+self.d_url_home