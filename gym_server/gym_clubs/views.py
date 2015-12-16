from rest_framework.viewsets import ModelViewSet
from .serializers import ClubSerializer
from .models import Club

class ClubViewSet(ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()

