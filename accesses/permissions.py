from rest_framework import permissions


class IsAdminOrGeneration(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.is_superuser | bool(request.user == obj.user)