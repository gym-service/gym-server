from rest_framework.routers import SimpleRouter
from .views import EventoViewSet, NotiziaViewSet, PressViewSet

router = SimpleRouter()
router.register('eventi', EventoViewSet)
router.register('notizie', NotiziaViewSet)
router.register('press', PressViewSet)

urlpatterns = router.urls


