from rest_framework import serializers

from farm.models import Farm, MilkCollection, FarmPayment


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = "__all__"


class MilkCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollection
        fields = "__all__"


class FarmPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmPayment
        fields = "__all__"