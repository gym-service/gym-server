from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class BaseContent(models.Model):

    ordine = models.IntegerField(null=False, blank=True, default=0)
    titolo = models.CharField(max_length=80, null=False)
    descrizione = models.CharField(max_length=2000, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True