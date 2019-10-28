from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if permissions.IsAdminUser:
            return True

        elif request.method == "DELETE":
            return False

        return obj.creator_id == request.user
