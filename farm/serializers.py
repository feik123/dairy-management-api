from rest_framework import serializers

from accounts.models import CustomUser
from farm.models import Farm, MilkCollection, FarmPayment


class FarmSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Farm
        fields = "__all__"

    def validate_user(self, user):
        if user.role != 'FARM':
            raise serializers.ValidationError(
                'A farm can only be assigned to a user with FARM role'
            )

        elif self.instance is not None and user != self.instance.user:
            raise serializers.ValidationError(
                "The farm's user cannot be changed"
            )

        return user


class MilkCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollection
        fields = "__all__"


class FarmPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmPayment
        fields = "__all__"