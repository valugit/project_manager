from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if obj.creator_id == request.user:
            return True

        return False


class IsMemberOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow members of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.user in obj.members.all():
            return True

        return False

