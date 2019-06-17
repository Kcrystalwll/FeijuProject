from django.shortcuts import render,HttpResponse,redirect
from rbac.models import *
from rbac.forms import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from mygas.views import getminfo

# Create your views here.
def group(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]
    if reinfo[1] == '超级管理员':
        groups = Group_info.objects.all()
    if reinfo[1] == '测试人员-管理员':
        groups = Group_info.objects.filter().exclude(groupname="超级管理员")
    context_dict['groups'] = groups

    gid = request.GET.get('gid')
    context_dict['gid'] = gid
    if gid:
        #多对多操作（反向查）
        obj = Group_info.objects.filter(id=gid).first()
        users = obj.user_info_set.all()
    else:
        if reinfo[1] == '超级管理员':
            users = User_info.objects.all()
        if reinfo[1] == '测试人员-管理员':
            users = User_info.objects.filter().exclude(username="wll")
    context_dict['users'] = users
    return render(request,'group.html',context_dict)

def group_add(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        form = GroupForm()
        context_dict['form'] = form
        return render(request, 'group_add.html', context_dict)
    else:
        form = GroupForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            Group_info.objects.create(**form.cleaned_data)
            return redirect('/group/')
        return render(request, 'group_add.html', context_dict)

def group_edit(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    if request.method == 'GET':
        row = Group_info.objects.filter(id=id).values(
            'groupname',
        ).first()
        form = GroupForm(initial=row)
        #POST提交时用到的ID必须是字符型，不可以是整数型
        context_dict['id'] = str(id)
        context_dict['form'] = form
        return render(request, 'group_edit.html', context_dict)
    else:
        form = GroupForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            groupname = form.cleaned_data['groupname']
            Group_info.objects.filter(id=id).update(groupname=groupname)
            return redirect('/group/')
        return render(request, 'group_edit.html', context_dict)

def group_del(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        idToDel = request.GET.get('p1')
        Group_info.objects.filter(id=idToDel).delete()
        return redirect('/group/')

def manulist(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user

    all_menu = Menu.objects.all()
    context_dict['all_menu'] = all_menu

    mid = request.GET.get('mid')
    context_dict['mid'] = mid   #传到前端
#筛选
    if mid:
        #Q:或
        all_permission = Permission_info.objects.filter(Q(menu_id=mid)|Q(parent__menu_id=mid))
    else:
        all_permission = Permission_info.objects.filter(Q(menu_id__isnull=False)|Q(parent__menu_id__isnull=False))
    context_dict['all_permission'] = all_permission
    return render(request,'manulist.html',context_dict)

def manulist_add(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        form = MenuForm()
        context_dict['form'] = form
        return render(request, 'manulist_add.html', context_dict)
    else:
        form = MenuForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            Menu.objects.create(**form.cleaned_data)
            return redirect('/manulist/')
        return render(request, 'manulist_add.html', context_dict)

def manulist_edit(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    if request.method == 'GET':
        row = Menu.objects.filter(id=id).values(
            'menu_name','icon','weight'
        ).first()
        form = MenuForm(initial=row)
        #POST提交时用到的ID必须是字符型，不可以是整数型(action)
        context_dict['id'] = str(id)
        context_dict['form'] = form
        return render(request, 'manulist_edit.html', context_dict)
    else:
        form = MenuForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            Menu.objects.filter(id=id).update(**form.cleaned_data)
            return redirect('/manulist/')
        return render(request, 'manulist_edit.html', context_dict)

def manulist_del(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        idToDel = request.GET.get('p1')
        Menu.objects.filter(id=idToDel).delete()
        return redirect('/manulist/')

def permissionlist_del(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        idToDel = request.GET.get('p1')
        Permission_info.objects.filter(id=idToDel).delete()
        return redirect('/manulist/')

def loginuser_add(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        form = UserForm()
        context_dict['form'] = form
        return render(request, 'loginuser_add.html', context_dict)
    else:
        form = UserForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password_ming = form.cleaned_data['password']
            password = make_password(password_ming, 'a', 'pbkdf2_sha256')
            group_id = form.cleaned_data['group_id']
            User_info.objects.create(
                username=username,
                password=password,
            )
            print(group_id)
            #增加多对多关系表
            obj = User_info.objects.filter(username=username).first()
            obj.group.add(group_id)
            return redirect('/group/')
        return render(request, 'loginuser_add.html', context_dict)

def pwd_reset(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = make_password('111111', 'a', 'pbkdf2_sha256')
        print(password)
        try:
            User_info.objects.filter(id=id).update(
                password=password,
            )
            return HttpResponse("1")
        except:
            return HttpResponse("2")

def loginuser_edit(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    if request.method == 'GET':
        row = User_info.objects.filter(id=id).values(
            'username', 'password',
        ).first()
        form = User_Form(initial=row)
        # POST提交时用到的ID必须是字符型，不可以是整数型(action里修改)
        context_dict['id'] = str(id)
        context_dict['form'] = form
        return render(request, 'loginuser_edit.html', context_dict)
    else:
        form = User_Form(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']   #应该是None
            password_ming = form.cleaned_data['password']
            password = make_password(password_ming,'a','pbkdf2_sha256')
            user_info = User_info.objects.get(id = id)
            user_info.password = password
            user_info.save()
            if user_info.username == user:
                return redirect('/logout/')
            else:
                return redirect('/group/')
        return render(request, 'loginuser_edit.html', context_dict)

def loginuser_del(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        idToDel = request.GET.get('p1')
        User_info.objects.filter(id=idToDel).delete()
        return redirect('/group/')



