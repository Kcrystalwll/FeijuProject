from django.db import models

# Create your models here.
class Menu(models.Model):
    #一级菜单 和二级菜单是一对多的关系

    menu_name = models.CharField(max_length=32,verbose_name='一级菜单名称',unique=True)
    icon = models.CharField(max_length=32, verbose_name='一级菜单图标', null=True, blank=True)
    weight = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = '菜单表'
        verbose_name = '菜单表'

    def __str__(self):
        return self.menu_name

#权限表
class Permission_info(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题')
    url = models.CharField(max_length=32, verbose_name='权限')

    #二级菜单
    #和Menu关联的是二级菜单；不关联Menu的不是二级菜单，也是不可以做菜单的权限
    menu = models.ForeignKey('Menu',verbose_name='一级菜单',null=True,blank=True)
    menu_name = models.CharField(max_length=32, verbose_name='二级菜单名称',null=True,blank=True)
    icon = models.CharField(max_length=32,verbose_name='二级菜单图标',null=True,blank=True)

    #三级菜单(自关联)
    parent = models.ForeignKey('Permission_info',null=True,blank=True)


    class Meta:
        verbose_name_plural = '权限表'
        verbose_name = '权限表'

    def __str__(self):
        return self.title

# 分组表
class Group_info(models.Model):
    groupname = models.CharField(max_length=32, verbose_name='组别')
    permission = models.ManyToManyField(to='Permission_info',verbose_name='组别拥有的权限')

    class Meta:
        verbose_name_plural = '分组表'
        verbose_name = '分组表'

    def __str__(self):
        return self.groupname

#用户表
class User_info(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    group = models.ManyToManyField(to='Group_info',verbose_name='用户所属组别')

    class Meta:
        verbose_name_plural = '用户表'
        verbose_name = '用户表'

    def __str__(self):
        return self.username