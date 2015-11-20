from __future__ import unicode_literals
from django.db import models
from django.conf import settings

SESSO_CHOICES = (
    ('M', 'Maschio'),
    ('F', 'Femmina'),
)

class GymUserInfo(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="gym_user")
    cognome = models.CharField(max_length=250, null=True, blank=True)
    nome = models.CharField(max_length=250, null=True, blank=True)
    data_nascita = models.DateField(verbose_name='Data di nascita', null=True, blank=True)    
    sesso = models.CharField(max_length=1, choices=SESSO_CHOICES, null=True, blank=True)
    telefono = models.CharField(verbose_name='Numero telefono',max_length=50, null=True, blank=True)
    indirizzo = models.CharField(max_length=500, null=True, blank=True)
    data_inizio_iscrizione = models.DateField(verbose_name='Data inizio iscrizione', null=True, blank=True)
    data_scadenza_iscrizione = models.DateField(verbose_name='Data fine iscrizione', null=True, blank=True)
    ultimo_accesso = models.DateTimeField(verbose_name='Data e ora ultimo accesso', null=True, blank=True)    
    
    def __unicode__(self):
        return u'%s %s - %s' % (self.nome, self.cognome, self.user.pk)

        
#class GymUserSubscription(models.Model):
#    pass


#class GymUserCertificate(models.Model):
#    pass
