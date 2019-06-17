from django import forms
from rbac.models import *
from mygas.views import getminfo

#分组
class GroupForm(forms.Form):
    groupname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )

#菜单
class MenuForm(forms.Form):
    menu_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    #fa的icon也可以
    icon = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    weight = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )

#权限
class PermissionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    menu_id = forms.IntegerField(
        widget=forms.Select(choices=Menu.objects.values_list('id','menu_name'),attrs={"class": "form-control"}),
        required=False
    )
    menu_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    # fa的icon也可以
    icon = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    parent_id = forms.CharField(
        widget=forms.Select(choices=Permission_info.objects.values_list('id','title'),attrs={"class": "form-control"}),
        required=True
    )

GROUP = (
    ('',''),
    (1,'生产厂商'),
    (2,'测试人员-管理员'),
    (3,'测试人员-操作员'),
)

#用户
class UserForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True
    )
    group_id = forms.CharField(
        widget=forms.Select(choices=GROUP,attrs={"class": "form-control"}),
        required=True
    )

class User_Form(forms.Form):
    username = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
        disabled=True
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True
    )