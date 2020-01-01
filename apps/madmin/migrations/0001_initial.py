# Generated by Django 2.2.9 on 2020-01-01 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlgRoleShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pri_name', models.CharField(max_length=64, verbose_name='权限名称')),
                ('model_name', models.CharField(max_length=64, verbose_name='模块名称')),
                ('controller_name', models.CharField(max_length=64, verbose_name='视图名称')),
                ('action_name', models.CharField(max_length=64, verbose_name='方法名称')),
                ('parent_id', models.IntegerField(default=0, verbose_name='父id')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=64, verbose_name='角色名称')),
                ('remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('ship', models.ManyToManyField(through='madmin.PlgRoleShip', to='madmin.Privilege')),
            ],
        ),
        migrations.AddField(
            model_name='plgroleship',
            name='privilege',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madmin.Privilege'),
        ),
        migrations.AddField(
            model_name='plgroleship',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madmin.Role'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=64, verbose_name='管理员名称')),
                ('password', models.CharField(db_column='pass', max_length=64, verbose_name='密码')),
                ('remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('state', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='最后登录ip')),
                ('role', models.ManyToManyField(to='madmin.Role', verbose_name='角色')),
            ],
        ),
    ]
