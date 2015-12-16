from rest_framework.serializers import ModelSerializer
from .models import Evento, Notizia, Press, Alert


class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento

class NotiziaSerializer(ModelSerializer):
    class Meta:
        model = Notizia

class PressSerializer(ModelSerializer):
    class Meta:
        model = Press

class AlertSerializer(ModelSerializer):
    class Meta:
        model = Alert
