from rest_framework.permissions import BasePermission


class IsOwnerOrFarmUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and user.role in ['OWNER', 'FARM']
        )