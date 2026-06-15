from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'phone',
        'is_active',
        'created_at',
    )

    list_filter = (
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
    )

