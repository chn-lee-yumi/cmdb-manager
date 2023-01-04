from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    class Meta:
        db_table = "project"

    name = models.CharField(max_length=16, primary_key=True)
    description = models.CharField(max_length=255, null=True)
    members = models.ManyToManyField(User, through='UserProjectPermission', through_fields=('project', 'user'))


class UserProjectPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    permission = models.CharField(max_length=5)  # admin/user


class Group(models.Model):
    class Meta:
        db_table = "group"

    name = models.CharField(max_length=16)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Role(models.Model):
    class Meta:
        db_table = "role"

    name = models.CharField(max_length=16)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Machine(models.Model):
    class Meta:
        db_table = 'machine'

    # id = models.CharField(max_length=36, primary_key=True)
    main_ip = models.CharField(max_length=15)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)  # 机器所属项目
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)  # 机器所属群组
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)  # 机器的角色
    device_system_info = models.JSONField(null=True)
    system_info = models.JSONField(null=True)
    cpu_info = models.JSONField(null=True)
    memory_info = models.JSONField(null=True)
    load_avg = models.JSONField(null=True)
    interfaces = models.JSONField(null=True)
    last_heartbeat = models.DateTimeField(null=True)
