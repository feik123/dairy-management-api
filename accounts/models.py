from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.TextChoices):
    OWNER = 'OWNER', 'Owner',
    STAFF = 'STAFF', 'Staff',
    FARM = 'FARM', 'Farm',
    CUSTOMER = 'CUSTOMER', 'Customer'

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER
    )
    phone = models.CharField(
        max_length=10,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_owner(self):
        return self.role == UserRole.OWNER
    
    @property
    def is_staff_member(self):
        return self.role == UserRole.STAFF
    
    @property
    def is_farm(self):
        return self.role == UserRole.FARM

    @property
    def is_customer(self):
        return self.role == UserRole.CUSTOMER

    def __str__(self):
        return self.username
