from rest_framework.routers import SimpleRouter
from .views import EventoViewSet, NotiziaViewSet, PressViewSet, AlertViewSet

router = SimpleRouter()
router.register('eventi', EventoViewSet)
router.register('notizie', NotiziaViewSet)
router.register('press', PressViewSet)
router.register('alert', AlertViewSet)

urlpatterns = router.urls


