from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in ['MANAGER', 'ADMIN']