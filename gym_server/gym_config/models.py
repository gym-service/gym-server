from __future__ import unicode_literals

from django.db import models

class GymConfig(models.Model):
    #example config for gym site
    slogan = models.CharField(max_length=100, null=True, blank=True)
    primary_color = models.CharField(max_length=12, null=True, blank=True, default="#FF0000")

