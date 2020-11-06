from rest_framework import permissions


class IsOwnerOrInRoom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed if the user is listed
        # in the users list of the room obj.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission are only allowed if the user is the room owner.
        return obj.owner == request.user
