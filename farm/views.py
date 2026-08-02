from rest_framework import viewsets

from .models import Farm, MilkCollection
from .serializers import FarmSerializer, MilkCollectionSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class MilkCollectionViewSet(viewsets.ModelViewSet):
    queryset = MilkCollection.objects.all()
    serializer_class = MilkCollectionSerializer