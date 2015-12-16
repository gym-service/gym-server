from rest_framework.viewsets import ModelViewSet
from .serializers import EventoSerializer
from .models import Evento


class EventoViewSet(ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

