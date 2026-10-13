from rest_framework.permissions import BasePermission


class IsOwnerOrFarmUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and user.role in ['OWNER', 'FARM']
        )


class IsOwnerForFarmWrite(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.role == 'OWNER':
            return True

        if user.role == 'FARM':
            return request.method in ['GET', 'HEAD', 'OPTIONS', ]

        return False
