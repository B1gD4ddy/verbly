from django.db import models
from django.utils import timezone

# Create your models here.

class Verb(models.Model):
    name = models.CharField('Verb Name', max_length=50, blank=True)
    
    prasent_ich = models.CharField(max_length=50)
    prasent_du = models.CharField(max_length=50)
    prasent_es = models.CharField(max_length=50)
    prasent_wir = models.CharField(max_length=50)
    prasent_ihr = models.CharField(max_length=50)
    prasent_sie = models.CharField(max_length=50)
    konjuktiv_prasent_ich = models.CharField(max_length=50)
    konjuktiv_prasent_du = models.CharField(max_length=50)
    konjuktiv_prasent_es = models.CharField(max_length=50)
    konjuktiv_prasent_wir = models.CharField(max_length=50)
    konjuktiv_prasent_ihr = models.CharField(max_length=50)
    konjuktiv_prasent_sie = models.CharField(max_length=50)
    
    prateritum_ich = models.CharField(max_length=50)
    prateritum_du = models.CharField(max_length=50)
    prateritum_es = models.CharField(max_length=50)
    prateritum_wir = models.CharField(max_length=50)
    prateritum_ihr = models.CharField(max_length=50)
    prateritum_sie = models.CharField(max_length=50)
    konjuktiv_prateritum_ich = models.CharField(max_length=50)
    konjuktiv_prateritum_du = models.CharField(max_length=50)
    konjuktiv_prateritum_es = models.CharField(max_length=50)
    konjuktiv_prateritum_wir = models.CharField(max_length=50)
    konjuktiv_prateritum_ihr = models.CharField(max_length=50)
    konjuktiv_prateritum_sie = models.CharField(max_length=50)
    
    perfekt_ich = models.CharField(max_length=70)
    perfekt_du = models.CharField(max_length=70)
    perfekt_es = models.CharField(max_length=70)
    perfekt_wir = models.CharField(max_length=70)
    perfekt_ihr = models.CharField(max_length=70)
    perfekt_sie = models.CharField(max_length=70)
    konjuktiv_perfekt_ich = models.CharField(max_length=70)
    konjuktiv_perfekt_du = models.CharField(max_length=70)
    konjuktiv_perfekt_es = models.CharField(max_length=70)
    konjuktiv_perfekt_wir = models.CharField(max_length=70)
    konjuktiv_perfekt_ihr = models.CharField(max_length=70)
    konjuktiv_perfekt_sie = models.CharField(max_length=70)
    
    plusquamperfekt_ich = models.CharField(max_length=70)
    plusquamperfekt_du = models.CharField(max_length=70)
    plusquamperfekt_es = models.CharField(max_length=70)
    plusquamperfekt_wir = models.CharField(max_length=70)
    plusquamperfekt_ihr = models.CharField(max_length=70)
    plusquamperfekt_sie = models.CharField(max_length=70)
    konjuktiv_plusquamperfekt_ich = models.CharField(max_length=70)
    konjuktiv_plusquamperfekt_du = models.CharField(max_length=70)
    konjuktiv_plusquamperfekt_es = models.CharField(max_length=70)
    konjuktiv_plusquamperfekt_wir = models.CharField(max_length=70)
    konjuktiv_plusquamperfekt_ihr = models.CharField(max_length=70)
    konjuktiv_plusquamperfekt_sie = models.CharField(max_length=70)
    
    futur1_ich = models.CharField(max_length=70)
    futur1_du = models.CharField(max_length=70)
    futur1_es = models.CharField(max_length=70)
    futur1_wir = models.CharField(max_length=70)
    futur1_ihr = models.CharField(max_length=70)
    futur1_sie = models.CharField(max_length=70)
    konjuktiv_futur1_ich = models.CharField(max_length=70)
    konjuktiv_futur1_du = models.CharField(max_length=70)
    konjuktiv_futur1_es = models.CharField(max_length=70)
    konjuktiv_futur1_wir = models.CharField(max_length=70)
    konjuktiv_futur1_ihr = models.CharField(max_length=70)
    konjuktiv_futur1_sie = models.CharField(max_length=70)
    konjuktiv2_futur1_ich = models.CharField(max_length=70)
    konjuktiv2_futur1_du = models.CharField(max_length=70)
    konjuktiv2_futur1_es = models.CharField(max_length=70)
    konjuktiv2_futur1_wir = models.CharField(max_length=70)
    konjuktiv2_futur1_ihr = models.CharField(max_length=70)
    konjuktiv2_futur1_sie = models.CharField(max_length=70)
    
    futur2_ich = models.CharField(max_length=70)
    futur2_du = models.CharField(max_length=70)
    futur2_es = models.CharField(max_length=70)
    futur2_wir = models.CharField(max_length=70)
    futur2_ihr = models.CharField(max_length=70)
    futur2_sie = models.CharField(max_length=70)
    konjuktiv_futur2_ich = models.CharField(max_length=70)
    konjuktiv_futur2_du = models.CharField(max_length=70)
    konjuktiv_futur2_es = models.CharField(max_length=70)
    konjuktiv_futur2_wir = models.CharField(max_length=70)
    konjuktiv_futur2_ihr = models.CharField(max_length=70)
    konjuktiv_futur2_sie = models.CharField(max_length=70)
    konjuktiv2_futur2_ich = models.CharField(max_length=70)
    konjuktiv2_futur2_du = models.CharField(max_length=70)
    konjuktiv2_futur2_es = models.CharField(max_length=70)
    konjuktiv2_futur2_wir = models.CharField(max_length=70)
    konjuktiv2_futur2_ihr = models.CharField(max_length=70)
    konjuktiv2_futur2_sie = models.CharField(max_length=70)
    
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

     
