from django.db import models


class Farm(models.Model):
    user = models.OneToOneField(
        to='accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name="farm",
    )

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MilkCollection(models.Model):
    farm = models.ForeignKey(
        to='Farm',
        on_delete=models.CASCADE,
        related_name='collections'
    )

    quantity_liters = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    collection_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Collected milk on {self.collection_date} from {self.farm.name}'


class FarmPayment(models.Model):
    farm = models.ForeignKey(
        to='Farm',
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Payment for {self.farm.name} on {self.payment_date}'

