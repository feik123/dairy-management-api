from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import CustomerRegistrationView, CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('register/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('', include(router.urls))
]