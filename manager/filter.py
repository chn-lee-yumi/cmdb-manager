from django_filters import FilterSet, filters

from .models import Machine, Role, Group, Project


class MachineFilter(FilterSet):
    main_ip = filters.CharFilter(field_name='main_ip', lookup_expr="icontains")
    project = filters.CharFilter(field_name='project__name', lookup_expr="iexact")
    group = filters.CharFilter(field_name='group', lookup_expr="iexact")
    role = filters.CharFilter(field_name='role', lookup_expr="iexact")

    class Meta:
        model = Machine
        fields = ('main_ip', 'project', 'group', 'role')


class ProjectFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr="icontains")

    class Meta:
        model = Project
        fields = ('name',)


class GroupFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr="icontains")
    project = filters.CharFilter(field_name='project__name', lookup_expr="iexact")

    class Meta:
        model = Group
        fields = ('name', 'project')


class RoleFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr="icontains")
    project = filters.CharFilter(field_name='project__name', lookup_expr="iexact")

    class Meta:
        model = Role
        fields = ('name', 'project')
