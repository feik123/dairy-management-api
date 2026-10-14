from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Farm, MilkCollection, FarmPayment
from .permissions import IsOwnerForFarmWrite
from .serializers import FarmSerializer, MilkCollectionSerializer, FarmPaymentSerializer


class FarmViewSet(viewsets.ModelViewSet):
    serializer_class = FarmSerializer
    permission_classes = [IsOwnerForFarmWrite]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'OWNER':
            return Farm.objects.all()

        return Farm.objects.filter(user=user)

class MilkCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = MilkCollectionSerializer
    permission_classes = [IsOwnerForFarmWrite]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'OWNER':
            return MilkCollection.objects.all()

        return MilkCollection.objects.filter(farm__user=user)


class FarmPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = FarmPaymentSerializer
    permission_classes = [IsOwnerForFarmWrite]

    def get_queryset(self):
        user = self.request.user

        if user.role == "OWNER":
            return FarmPayment.objects.all()

        return FarmPayment.objects.filter(farm__user=user)