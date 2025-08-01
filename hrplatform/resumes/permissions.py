from rest_framework import permissions
from users.models import Profile, Role


class ResumePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'profile'):
            return False

        if request.user.profile.role == Role.ADMIN:
            return True

        if request.user.profile.role == Role.HR:
            return request.method in permissions.SAFE_METHODS

        return True

    def has_object_permission(self, request, view, obj):
        if not hasattr(request.user, 'profile'):
            return False

        if request.user.profile.role == Role.ADMIN:
            return True

        if request.user.profile.role == Role.HR:
            return request.method in permissions.SAFE_METHODS

        return obj.user == request.user