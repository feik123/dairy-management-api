from rest_framework import viewsets

from .models import Farm, MilkCollection, FarmPayment
from .serializers import FarmSerializer, MilkCollectionSerializer, FarmPaymentSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class MilkCollectionViewSet(viewsets.ModelViewSet):
    queryset = MilkCollection.objects.all()
    serializer_class = MilkCollectionSerializer


class FarmPaymentViewSet(viewsets.ModelViewSet):
    queryset = FarmPayment.objects.all()
    serializer_class = FarmPaymentSerializer