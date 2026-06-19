from django.db import models

class CustomerType(models.TextChoices):
    STORE = 'STORE', 'Store',
    HOTEL = 'HOTEL', 'Hotel',
    RESTAURANT = 'RESTAURANT', 'Restaurant',
    PRIVATE = 'PRIVATE', 'Private'

class Customer(models.Model):
    user = models.OneToOneField(
        to='accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='customer',
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    customer_type = models.CharField(
        max_length=20,
        choices=CustomerType.choices,
    )

    phone_number = models.CharField(max_length=20)

    address = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name