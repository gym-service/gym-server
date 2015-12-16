from rest_framework.routers import SimpleRouter
from .views import ClubViewSet

router = SimpleRouter()
router.register('club', ClubViewSet)

urlpatterns = router.urls


