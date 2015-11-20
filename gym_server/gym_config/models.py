from __future__ import unicode_literals

from django.db import models

class GymConfig(models.Model):
    #example config for gym site
    chiave = models.CharField(max_length=100)
    valore = models.CharField(max_length=100, null=True, blank=True)
    

