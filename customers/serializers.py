from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Customer

User = get_user_model()

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='This username is already taken!'
            )
        ]
    )

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={'input_type':'password'},
    )
    phone = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
        max_length=10,
    )

    class Meta:
        model = Customer
        fields = [
            'id',
            'username',
            'password',
            'phone',
            'name',
            'customer_type',
            'phone_number',
            'address',
        ]
        read_only_fields = ['id']

    @transaction.atomic
    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        phone = validated_data.pop('phone', '')

        user = User(
            username=username,
            role='CUSTOMER',
            phone=phone,
        )
        user.set_password(password)
        user.save()

        customer = Customer.objects.create(
            user=user,
            **validated_data,
        )

        return customer

