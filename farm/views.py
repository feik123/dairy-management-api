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
    queryset = MilkCollection.objects.all()
    serializer_class = MilkCollectionSerializer
    permission_classes = [IsAuthenticated]


class FarmPaymentViewSet(viewsets.ModelViewSet):
    queryset = FarmPayment.objects.all()
    serializer_class = FarmPaymentSerializer
    permission_classes = [IsAuthenticated]