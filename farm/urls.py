from rest_framework.routers import DefaultRouter

from farm.views import FarmViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet)

urlpatterns = router.urls