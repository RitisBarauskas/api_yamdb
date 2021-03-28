# from rest_framework.permissions import SAFE_METHODS, BasePermission


# class IsModerator(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.is_modertor
    
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user.is_moderator


# class IsAdmin(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.is_admin
    
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user.is_admin


# class IsAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS or request.user.is_authenticated and request.user.is_admin

#     def has_object_permission(self, request, view, obj):
#         return request.method in SAFE_METHODS or request.user.is_authenticated and request.user.is_admin


# class IsSuperuser(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.is_superuser

#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user.is_superuser