from rest_framework.routers import DefaultRouter

from farm.views import FarmViewSet, MilkCollectionViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet)
router.register('collections', MilkCollectionViewSet)
urlpatterns = router.urls