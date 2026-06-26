from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'


class Order(models.Model):
    customer = models.ForeignKey(
        to='customers.Customer',
        on_delete=models.PROTECT,
        related_name='orders'
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Order #{self.pk} for {self.customer.name}, phone {self.customer.phone_number}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        to='Order',
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        to='products.Product',
        on_delete=models.PROTECT,
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return self.product.name
