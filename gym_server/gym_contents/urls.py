from rest_framework.routers import SimpleRouter
from .views import EventoViewSet

router = SimpleRouter()
router.register('eventi', EventoViewSet)

urlpatterns = router.urls


