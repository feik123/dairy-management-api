from tkinter.font import names

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)

    description = models.TextField(blank=True)

    unit = models.CharField(
        max_length=20,
        default='kg'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name