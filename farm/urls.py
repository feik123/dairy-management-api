from rest_framework.routers import DefaultRouter

from farm.views import FarmViewSet, MilkCollectionViewSet, FarmPaymentViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet, basename='farm')
router.register('collections', MilkCollectionViewSet, basename='collection')
router.register('payments', FarmPaymentViewSet, basename='payment')

urlpatterns = router.urls