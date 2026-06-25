from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'customer_type',
        'phone_number',
        'address',
        'is_active'
    )

    list_filter = (
        'customer_type',
        'address'
    )

    search_fields = (
        'name',
        'phone_number'
    )

