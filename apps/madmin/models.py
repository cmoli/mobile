from django.db import models


class Privilege(models.Model):
    pri_name = models.CharField(verbose_name='权限名称', max_length=64)
    model_name = models.CharField(verbose_name='模块名称', max_length=64)
    controller_name = models.CharField(verbose_name='视图名称', max_length=64)
    action_name = models.CharField(verbose_name='方法名称', max_length=64)
    parent_id = models.IntegerField(verbose_name='父id', default=0)


class Role(models.Model):
    role_name = models.CharField(verbose_name='角色名称', max_length=64)
    remark = models.CharField(verbose_name='备注', max_length=64, blank=True, null=True)
    ship = models.ManyToManyField(Privilege, through='PlgRoleShip')


class Admin(models.Model):
    admin_name = models.CharField(verbose_name='管理员名称', max_length=64)
    password = models.CharField(db_column='pass', verbose_name='密码', max_length=64)
    remark = models.CharField(verbose_name='备注', max_length=64, blank=True, null=True)
    state = models.SmallIntegerField(verbose_name='状态', default=1)
    add_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_ip = models.GenericIPAddressField(verbose_name='最后登录ip', blank=True, null=True)
    role = models.ManyToManyField(Role, verbose_name='角色')


class PlgRoleShip(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)
    remark = models.CharField(verbose_name='备注', max_length=64, blank=True, null=True)

