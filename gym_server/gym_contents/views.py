from rest_framework.viewsets import ModelViewSet
from .serializers import EventoSerializer, NotiziaSerializer, PressSerializer, AlertSerializer, \
                         VideoSerializer, GallerySerializer, ImmaginigallerieSerializer
from .models import Evento, Notizia, Press, Alert, Video, Gallery, Immaginigallerie

class ModelViewSetWithStato(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.id and user.is_staff:
            return self.queryset.exclude(stato=0)
        return self.queryset.filter(stato=2)


class EventoViewSet(ModelViewSetWithStato):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

class NotiziaViewSet(ModelViewSetWithStato):
    serializer_class = NotiziaSerializer
    queryset = Notizia.objects.all()
    
class PressViewSet(ModelViewSetWithStato):
    serializer_class = PressSerializer
    queryset = Press.objects.all()

class AlertViewSet(ModelViewSetWithStato):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()

class VideoViewSet(ModelViewSetWithStato):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class GalleryViewSet(ModelViewSetWithStato):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()

class ImmaginigallerieViewSet(ModelViewSetWithStato):
    serializer_class = ImmaginigallerieSerializer
    queryset = Immaginigallerie.objects.all()

