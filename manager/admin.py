from django.contrib import admin

from .models import Machine, Project, Group, Role, UserProjectPermission

admin.site.register(Machine)
admin.site.register(Project)
admin.site.register(Group)
admin.site.register(Role)
admin.site.register(UserProjectPermission)
admin.site.site_header = 'CMDB管理后台'
