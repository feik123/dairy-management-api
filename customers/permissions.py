from rest_framework.permissions import BasePermission


class IsOwnerStaffOrCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and user.role in ['OWNER', 'STAFF', 'CUSTOMER']
        )

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role in ['OWNER', 'STAFF']:
            return True

        if user.role == 'CUSTOMER':
            return obj.user.id == user.id and request.method in [
                'GET',
                'HEAD',
                'OPTIONS',
            ]

        return False