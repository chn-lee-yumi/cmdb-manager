from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from cmdb_manager.settings import CACHE_TTL
from .filter import MachineFilter, ProjectFilter, GroupFilter, RoleFilter
from .models import Machine, Project, Group, Role, UserProjectPermission
from .permissions import IsInProject
from .serializers import MachineSerializer, ProjectSerializer, GroupSerializer, RoleSerializer


class CMDBModelViewSet(ModelViewSet):

    def get_queryset(self):
        # 必须指定项目，否则报错
        project = self.request.GET.get('project')
        if not project:
            raise PermissionError('You must specify a project.')
        # 判断是否有项目权限
        user = self.request.user
        user_permissions = UserProjectPermission.objects.filter(user=user, project=project).all()
        if not user_permissions:
            raise PermissionError('You do not have permission in the project.')
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        # 只有项目admin才有权限创建
        user = request.user
        project = request.data['project']
        user_permissions = UserProjectPermission.objects.filter(user=user, project=project).all()
        print(user_permissions)
        if not user_permissions or user_permissions[0].permission != "admin":
            raise PermissionError('You do not have permission to create.')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # 只有项目admin才有权限修改
        user = request.user
        project = self.request.GET.get('project')
        user_permissions = UserProjectPermission.objects.filter(user=user, project=project).all()
        if not user_permissions or user_permissions[0].permission != "admin":
            raise PermissionError('You do not have permission to update.')
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # 只有项目admin才有权限删除
        user = request.user
        project = self.request.GET.get('project')
        user_permissions = UserProjectPermission.objects.filter(user=user, project=project).all()
        if not user_permissions or user_permissions[0].permission != "admin":
            raise PermissionError('You do not have permission to destroy.')
        return super().destroy(request, *args, **kwargs)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsInProject]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = ProjectFilter
    filterset_fields = ['name', ]
    search_fields = ('name',)

    def get_queryset(self):
        # 过滤掉用户没权限的项目
        user = self.request.user
        user_permissions = UserProjectPermission.objects.filter(user=user)
        return Project.objects.filter(userprojectpermission__in=user_permissions)


# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MachineViewSet(CMDBModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = MachineFilter
    filterset_fields = ['main_ip']
    search_fields = ('main_ip',)


# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class GroupViewSet(CMDBModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = GroupFilter
    filterset_fields = ['name', 'project']
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        # 判断项目内是否存在重名群组
        project = request.data['project']
        group_name = request.data['name']
        has_exist_group = Group.objects.filter(project=project, name=group_name).exists()
        if has_exist_group:
            raise NameError('Group exists.')
        return super().create(request, *args, **kwargs)


# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class RoleViewSet(CMDBModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = RoleFilter
    filterset_fields = ['name', 'project']
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        # 判断项目内是否存在重名角色
        project = request.data['project']
        role_name = request.data['name']
        has_exist_role = Role.objects.filter(project=project, name=role_name).exists()
        if has_exist_role:
            raise NameError('Role exists.')
        return super().create(request, *args, **kwargs)
