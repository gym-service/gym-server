from rest_framework.serializers import ModelSerializer
from .models import Evento


class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
