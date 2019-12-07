from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users edit their own profile"""
    def has_object_permission(self,request,view,obj):
        """check user is trying to create their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users update their own status"""
    def has_object_permission(self,request,view,obj):
        """check user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
