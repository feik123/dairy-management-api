from django.template.context_processors import request
from rest_framework import generics, permissions, viewsets

from customers.models import Customer
from customers.permissions import IsOwnerStaffOrCustomer
from customers.serializers import CustomerRegistrationSerializer, CustomerSerializer


class CustomerRegistrationView(generics.CreateAPIView):
    serializer_class = CustomerRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsOwnerStaffOrCustomer]

    def get_queryset(self):
        user = self.request.user

        if user.role in ['OWNER', 'STAFF']:
            return Customer.objects.all()

        return Customer.objects.filter(user=user)
