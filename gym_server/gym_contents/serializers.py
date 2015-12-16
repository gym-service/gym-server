from rest_framework.serializers import ModelSerializer
from .models import Evento, Notizia, Press, Alert, Video, Gallery, Immaginigallerie


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

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video

class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery

class ImmaginigallerieSerializer(ModelSerializer):
    class Meta:
        model = Immaginigallerie