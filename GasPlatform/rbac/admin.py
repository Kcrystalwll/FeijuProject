from django.contrib import admin
from rbac.models import *

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_name','icon','weight']
    list_editable = ['menu_name','icon','weight']

class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title','url','menu','menu_name','icon','parent']
    list_editable = ['url','menu','menu_name','icon','parent']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['groupname']
    # list_editable = ['groupname']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    # list_editable = ['username']

admin.site.register(Permission_info,PermissionAdmin)
admin.site.register(Group_info,GroupAdmin)
admin.site.register(User_info,UserAdmin)
admin.site.register(Menu,MenuAdmin)