from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit thier own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:  #check if the request is get method then you can get the data as you can't update any data using get method
            return True
        
        return obj.id == request.user.id    #or user edit his own profile


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id