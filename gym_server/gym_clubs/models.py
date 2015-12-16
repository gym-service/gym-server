from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class Club(models.Model):

    ordine = models.IntegerField(null=False, blank=True, default=0)
    nome = models.CharField(max_length=80, null=False)
    descrizione_breve = models.CharField(max_length=300, null=True, blank=True)
    descrizione = models.TextField(max_length=2000, null=True, blank=True)
    data_apertura = models.DateTimeField(auto_now=True)
    immagine = models.ImageField(null=True, blank=True, upload_to="immagini")
    allegato = models.FileField(null=True, blank=True, upload_to="allegati")
    indirizzo = models.TextField(max_length=2000, null=True, blank=True)
    # TODO -> indirizzo geografico 

    class Meta:
      verbose_name = "Club"
      verbose_name_plural = "Clubs"


