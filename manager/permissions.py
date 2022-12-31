from rest_framework import permissions

from .models import UserProjectPermission


class IsInProject(permissions.BasePermission):
    """
    判断用户是否加入了项目
    """

    def has_object_permission(self, request, view, obj):
        return UserProjectPermission.objects.filter(user_id=request.user.id, project_id=obj.name).exists()
