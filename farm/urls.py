from rest_framework.routers import DefaultRouter

from farm.views import FarmViewSet, MilkCollectionViewSet, FarmPaymentViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet)
router.register('collections', MilkCollectionViewSet)
router.register('payments', FarmPaymentViewSet)

urlpatterns = router.urls