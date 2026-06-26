from django.contrib import admin

from farm.models import Farm, MilkCollection, FarmPayment


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'address',
        'is_active',
    )

    search_fields = (
        'name',
        'phone_number',
    )

@admin.register(MilkCollection)
class MilkCollectionAdmin(admin.ModelAdmin):
    list_display = (
        'farm',
        'collection_date',
        'quantity_liters',
    )

    list_filter = (
        'collection_date',
    )


@admin.register(FarmPayment)
class FarmPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'farm',
        'payment_date',
        'amount',
    )