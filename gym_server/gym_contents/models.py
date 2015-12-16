from __future__ import unicode_literals
from django.conf import settings
from django.db import models

STATO_CHOICES = [
    [0, 'Non pubblicato'],
    [1, 'In prova'],
    [2, 'Pubblicato']
]

class BaseContent(models.Model):

    ordine = models.IntegerField(null=False, blank=True, default=0)
    titolo = models.CharField(max_length=80, null=False)
    sottotitolo = models.CharField(max_length=80, null=True, blank=True)
    descrizione = models.CharField(max_length=2000, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stato = models.IntegerField(choices = STATO_CHOICES, default=0, blank=True)
    promosso = models.BooleanField(blank=True, default=False)
    url = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True


class Evento(BaseContent):

    immagine = models.ImageField(null=True, blank=True, upload_to="immagini")
    allegato = models.FileField(null=True, blank=True, upload_to="allegati")
    data = models.DateField(null=True, blank=True)
    luogo = models.CharField(max_length=30, null=True, blank=True)
    descrizione_luogo = models.TextField(null=True, blank=True)
