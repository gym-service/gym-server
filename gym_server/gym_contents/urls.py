from rest_framework.routers import SimpleRouter
from .views import EventoViewSet, NotiziaViewSet, PressViewSet, AlertViewSet, VideoViewSet, \
                   GalleryViewSet, ImmaginigallerieViewSet

router = SimpleRouter()
router.register('eventi', EventoViewSet)
router.register('notizie', NotiziaViewSet)
router.register('press', PressViewSet)
router.register('alert', AlertViewSet)
router.register('video', VideoViewSet)
router.register('gallery', GalleryViewSet)
router.register('immaginigallerie', ImmaginigallerieViewSet)

urlpatterns = router.urls


