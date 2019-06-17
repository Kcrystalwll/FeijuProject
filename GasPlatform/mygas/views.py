from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from mygas.forms import *
from mygas.models import *
from rbac.models import *   #权限
from mygas.utils.pager import PageInfo    #分页
from django.db import IntegrityError
import datetime
import json
import time
from django.http import JsonResponse
from rbac.server.init_permission import init_permission
from django.contrib.auth.hashers import make_password, check_password  #加密解密
import xlwt
from io import BytesIO
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q

def prin(request):
    return render(request, 'print.html')

# Create your views here.
def login(request):
    context_dict={}
    if request.method == 'GET':
        form = LoginForm()
        context_dict['msg'] = ""
        context_dict['form'] = form
        return render(request, 'login.html', context_dict)
    else:
        form = LoginForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            username = request.POST.get('username')
            password_ming = request.POST.get('password')  #输入的密码
            print(username)
            print(password_ming)
            user = User_info.objects.filter(username=username).first()
            print(user)
            # print(user.password)   #数据库里存的密码
            # print(type(user.group.all()))  #queryset
            # print(user.group.all().first().groupname)
            if user is not None and check_password(password_ming, user.password):
                #登陆成功
                print(str(user) + '登陆成功')
                init_permission(request,user)
                request.session['user'] = username
                return HttpResponseRedirect('/index/')
            else:
                context_dict['msg'] = "用户名或密码有误，请重新输入！"
        else:
            context_dict['msg'] = "请按要求输入用户名和密码"
        return render(request, 'login.html', context_dict)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def index(request):
    context_dict = {}
    user = request.session.get('user','')
    context_dict['user'] = user
    return render(request,'base.html',context_dict)

#获得登录的厂商对应的ID
def getminfo(request):
    user = request.session.get('user', '')  #获得登录的用户
    username = User_info.objects.get(username=user)
    uid = username.id  # 获得登录用户的ID
    # print(uid)
    groupname = username.group.all().first().groupname  # 获得登录用户所属组别的组名
    # print(groupname)
    ucode = user[-2:]  # 获得登录用户后两位编码  仅厂商名字后两位有编码
    # print(ucode)
    # print("用户所属组别是：" + groupname)
    # 登录用户是厂商时，获得厂商id
    try:
        manu = Manufacture.objects.get(code=ucode)
        # print(manu.ManufactureName)
        mid_u = manu.id
        # print(manu.id)
    # 不是厂商只获得用户名即可
    except Exception as e:
        mid_u = username.username
        # print(username.username)
    return user, groupname, mid_u, uid  # tuple()

# 导出excel数据
def export_excel(request):
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=order.xls'
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('order-sheet')

    # 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
    style_heading = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour 0x19;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """)

    # 写入文件标题
    sheet.write(0,0,'序号',style_heading)
    sheet.write(0,1,'燃气表表号',style_heading)
    sheet.write(0,2,'燃气表类型',style_heading)
    sheet.write(0,3,'生产厂商',style_heading)
    sheet.write(0,4,'生产日期',style_heading)

    # 写入数据
    data_row = 1
    # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
    for i in GS_MeterTypeInfo.objects.all():
        # 格式化datetime
        pro_time = i.TimeOfProduce.strftime('%Y-%m-%d')
        sheet.write(data_row,0,i.id)
        sheet.write(data_row,1,i.MeterId)
        sheet.write(data_row,2,i.MeterType)
        sheet.write(data_row,3,i.ManufactureName.ManufactureName)
        sheet.write(data_row,4,pro_time)
        data_row = data_row + 1

    # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response

#显示所有录入的燃气表及其状态
def data(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]   #用户名传给前端
    search_dict = dict()
    if request.method == 'GET':
        q_form = MeterQueryForm1()
        context_dict['q_form'] = q_form
        if reinfo[1] != '生产厂商':
            # 分页
            all_count = GS_MeterTypeInfo.objects.filter(IsSubmit=0).count()
            current_page = request.GET.get('page')
            page_info = PageInfo(current_page, all_count, 10, '/data/', 11)
            meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=0)[page_info.start():page_info.end()]
            context_dict['meter_list'] = meter_list
            context_dict['page_info'] = page_info  # 不要忘了传到前端
            return render(request, 'data.html', context_dict)
        else:  #是生产厂商时,只能拿到登录用户（厂商）的表信息
            # 分页
            all_count = GS_MeterTypeInfo.objects.filter(IsSubmit=0,ManufactureName_id=reinfo[2]).count()
            current_page = request.GET.get('page')
            page_info = PageInfo(current_page, all_count, 10, '/data/', 11)
            meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=0,ManufactureName_id=reinfo[2])[page_info.start():page_info.end()]
            context_dict['meter_list'] = meter_list
            context_dict['page_info'] = page_info  # 不要忘了传到前端
            return render(request, 'data.html', context_dict)
    else:
        q_form = MeterQueryForm1(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            if reinfo[1] != '生产厂商':
                info = GS_MeterTypeInfo.objects.filter(IsSubmit=0, **search_dict)
                context_dict['meter_list'] = info
                return render(request, 'data.html', context_dict)
            else:
                info = GS_MeterTypeInfo.objects.filter(IsSubmit=0,ManufactureName_id=reinfo[2], **search_dict)
                context_dict['meter_list'] = info
                return render(request, 'data.html', context_dict)
        else:
            q_form = MeterQueryForm1()
            return HttpResponse("not found 404")

#提交录入的数据
def submit(request):
    if request.method == 'POST':
        MeterToSub = request.POST['MeterId']
        try:
            meter = GS_MeterTypeInfo.objects.get(MeterId=MeterToSub)
            meter.IsSubmit = 1
            meter.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")

#审核状态判断
def getcheckstate(meterstate):
    if meterstate == "待审核":
        state = 0
        con_state = 0
    elif meterstate == "通过":
        state = 1
        con_state = 1
    elif meterstate == "不通过":
        state = 1
        con_state = 0
    return state,con_state

#提交后的燃气表审核结果
def dataresult(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  #用户名传给前端
    if request.method == 'GET':
        q_form = MeterQueryForm2()
        context_dict['q_form'] = q_form
        if reinfo[1] != '生产厂商':
            # 分页
            all_count = GS_MeterTypeInfo.objects.filter(IsSubmit=1).count()
            current_page = request.GET.get('page')
            page_info = PageInfo(current_page, all_count, 10, '/dataresult/', 11)
            #待审核、通过、不通过
            meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=1)[page_info.start():page_info.end()]
            context_dict['meter_list'] = meter_list
            context_dict['page_info'] = page_info    #不要忘了传到前端
            return render(request, 'dataresult.html', context_dict)
        else:
            # 分页
            all_count = GS_MeterTypeInfo.objects.filter(IsSubmit=1,ManufactureName_id=reinfo[2]).count()
            current_page = request.GET.get('page')
            page_info = PageInfo(current_page, all_count, 10, '/dataresult/', 11)
            # 待审核、通过、不通过
            meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=1,ManufactureName_id=reinfo[2])[page_info.start():page_info.end()]
            for m in meter_list:
                print(m.IsTest)
            context_dict['meter_list'] = meter_list
            context_dict['page_info'] = page_info  # 不要忘了传到前端
            return render(request, 'dataresult.html', context_dict)
    else:
        q_form = MeterQueryForm2(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            meterstate = q_form.cleaned_data['MeterState']
            subtime = q_form.cleaned_data['Subtime']
            if reinfo[1] != '生产厂商':
                if meterid == "" and metertype == "" and meterstate == "" and subtime == None:
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                if meterid:
                    try:
                        meter = GS_MeterTypeInfo.objects.get(MeterId=meterid, IsSubmit=1)
                    except:
                        meter = None
                    context_dict['meter'] = meter
                elif metertype and meterstate == "" and subtime == None:
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype, IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and metertype == "" and subtime == None:
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif subtime and metertype == '' and meterstate == '':
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(Subtime__year=subtime.year,Subtime__month=subtime.month,Subtime__day=subtime.day,IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and metertype and subtime == None:
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype,IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and subtime and metertype == '':
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(Subtime__year=subtime.year,Subtime__month=subtime.month,Subtime__day=subtime.day,IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif metertype and subtime and meterstate == '':
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype,Subtime__year=subtime.year,
                                                                     Subtime__month=subtime.month,
                                                                     Subtime__day=subtime.day, IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and subtime and metertype:
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype,Subtime__year=subtime.year,Subtime__month=subtime.month,Subtime__day=subtime.day,IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1)
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                return render(request, 'dataresult.html', context_dict)
            else:
                if meterid == "" and metertype == "" and meterstate == "" and subtime == None:
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                if meterid:
                    try:
                        meter = GS_MeterTypeInfo.objects.get(MeterId=meterid, IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter = None
                    context_dict['meter'] = meter
                elif metertype and meterstate == "" and subtime == None:
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype, IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and metertype == "" and subtime == None:
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif subtime and metertype == '' and meterstate == '':
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(Subtime__year=subtime.year,Subtime__month=subtime.month,Subtime__day=subtime.day,IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and metertype and subtime == None:
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype,IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and subtime and metertype == '':
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(Subtime__year=subtime.year,Subtime__month=subtime.month,Subtime__day=subtime.day,IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif metertype and subtime and meterstate == '':
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype,Subtime__year=subtime.year,
                                                                     Subtime__month=subtime.month,
                                                                     Subtime__day=subtime.day, IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                elif meterstate and subtime and metertype:
                    s = getcheckstate(meterstate)
                    try:
                        meter_list = GS_MeterTypeInfo.objects.filter(MeterType=metertype,Subtime__year=subtime.year,Subtime__month=subtime.month,Subtime__day=subtime.day,IsDataChecked=s[0],DataCheckedResult=s[1],IsSubmit=1,ManufactureName_id=reinfo[2])
                    except:
                        meter_list = None
                    context_dict['meter_list'] = meter_list
                return render(request, 'dataresult.html', context_dict)
        else:
            q_form = MeterQueryForm2()
            return HttpResponse("not found 404")

#数据录入的燃气表类型选择
def datainput(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    if request.method == 'GET':
        form = MeterTypeForm()
        context_dict['msg'] = ""
        context_dict['form'] = form
        return render(request, 'datainput.html',context_dict)
    else:
        form = MeterTypeForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            MeterId = form.cleaned_data['MeterId']
            MeterType = form.cleaned_data['MeterType']
            ManufactureName_id = form.cleaned_data['ManufactureName_id']
            TimeOfProduce = form.cleaned_data['TimeOfProduce']
            request.session['MeterId'] = MeterId
            request.session['MeterType'] = MeterType
            request.session['ManufactureName_id'] = ManufactureName_id
            request.session['TimeOfProduce'] = TimeOfProduce
            try:
                meter2 = Meter_Test.objects.get(MeterId=MeterId)
            except:
                meter2 = None
            if meter2:
                context_dict['test'] = 1  #测试中
                return render(request, 'sub-edit-check-result.html', context_dict)
            else:
                try:
                    meter1 = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                except:
                    meter1 = None
                if meter1:
                    if MeterType == 'IC卡-膜式表':
                        url = '/edit_ic_msb/?p1=' + str(meter1.id) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "IC卡-修正仪":
                        url = '/edit_ic_xzy/?p1=' + str(meter1.id) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "IC卡-超声波":
                        url = '/edit_ic_csb/?p1=' + str(meter1.id) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "膜式表":
                        url = '/edit_msb/?p1=' + str(meter1.id) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "修正仪":
                        url = '/edit_xzy/?p1=' + str(meter1.id) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "超声波":
                        url = '/edit_csb/?p1=' + str(meter1.id) + '&p2=' + MeterType
                        return redirect(url)
                else:
                    if MeterType == "膜式表":
                        url = '/datainput_msb/?p1=' + str(MeterId) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "修正仪":
                        url = '/datainput_xzy/?p1=' + str(MeterId) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "超声波":
                        url = '/datainput_csb/?p1=' + str(MeterId) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == 'IC卡-膜式表':
                        url = '/datainput_ic_msb/?p1=' + str(MeterId) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "IC卡-修正仪":
                        url = '/datainput_ic_xzy/?p1=' + str(MeterId) + '&p2=' + MeterType
                        return redirect(url)
                    if MeterType == "IC卡-超声波":
                        url = '/datainput_ic_csb/?p1=' + str(MeterId) + '&p2=' + MeterType
                        return redirect(url)
        else :
            context_dict['msg'] = form.errors
        return render(request, 'datainput.html', context_dict)

#录入IC卡-膜式表数据
def datainput_ic_msb(request):
    context_dict={}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    MeterId = request.session.get("MeterId", "")
    context_dict['MeterId'] = MeterId
    MeterType = request.session.get("MeterType", "")
    context_dict['MeterType'] = MeterType
    ManufactureName_id = request.session.get("ManufactureName_id", "")
    TimeOfProduce = request.session.get("TimeOfProduce", "")
    if request.method == 'GET':
        form1 = Meter_ICForm()
        form2 = Meter_MSBForm()
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['msg1'] = ""
        context_dict['msg2'] = ""
        return render(request,'datainput_ic_msb.html',context_dict)
    else:
        form1 = Meter_ICForm(request.POST)
        form2 = Meter_MSBForm(request.POST)
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        if form1.is_valid():
            if form2.is_valid():
                try:
                   subtime = datetime.datetime.now()  #这个subtime可以说是厂商编辑时间
                   GS_MeterTypeInfo.objects.create(
                       MeterId=MeterId,
                       MeterType=MeterType,
                       ManufactureName_id=ManufactureName_id,
                       TimeOfProduce=TimeOfProduce,
                       Subtime = subtime,
                       user_id = reinfo[3]
                   )
                   meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                   GS_MeterInfo_IC.objects.create(MeterId=MeterId, MeterTypeId_id=meter.id,**form1.cleaned_data)
                   GS_MeterInfo_MSB.objects.create(MeterId=MeterId,MeterTypeId_id=meter.id, **form2.cleaned_data)
                   context_dict['success_input'] = 1  # 录入成功
                except IntegrityError:
                   context_dict['duplicate_input'] = 3  # 表号重复
            else:
                # 数据不符合要求,本页面回滚，但不刷新
                context_dict['msg2'] = form2.errors
                return render(request, 'datainput_ic_msb.html', context_dict)
        else:
            # 数据不符合要求,本页面回滚，但不刷新
            context_dict['msg1'] = form1.errors
            return render(request, 'datainput_ic_msb.html', context_dict)
        return render(request,'sub-edit-check-result.html',context_dict)

#录入IC卡-修正仪数据
def datainput_ic_xzy(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    MeterId = request.session.get("MeterId", "")
    context_dict['MeterId'] = MeterId
    MeterType = request.session.get("MeterType", "")
    context_dict['MeterType'] = MeterType
    ManufactureName_id = request.session.get("ManufactureName_id", "")
    TimeOfProduce = request.session.get("TimeOfProduce", "")
    if request.method == 'GET':
        form1 = Meter_ICForm()
        form2 = Meter_XZYForm()
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['msg1'] = ""
        context_dict['msg2'] = ""
        return render(request, 'datainput_ic_xzy.html', context_dict)
    else:
        form1 = Meter_ICForm(request.POST)
        form2 = Meter_XZYForm(request.POST)
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        if form1.is_valid():
            if form2.is_valid():
                try:
                    subtime = datetime.datetime.now()
                    GS_MeterTypeInfo.objects.create(
                           MeterId=MeterId,
                           MeterType=MeterType,
                           ManufactureName_id=ManufactureName_id,
                           TimeOfProduce=TimeOfProduce,
                           Subtime=subtime,
                           user_id = reinfo[3]
                       )
                    meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                    GS_MeterInfo_IC.objects.create(MeterId=MeterId, MeterTypeId_id=meter.id,**form1.cleaned_data)
                    GS_MeterInfo_XZY.objects.create(MeterId=MeterId,MeterTypeId_id=meter.id, **form2.cleaned_data)
                    context_dict['success_input'] = 1  # 录入成功
                except IntegrityError:
                    context_dict['duplicate_input'] = 3  # 表号重复
            else:
                # 数据不符合要求,本页面回滚，但不刷新
                context_dict['msg2'] = form2.errors
                return render(request, 'datainput_ic_xzy.html', context_dict)
        else:
            # 数据不符合要求,本页面回滚，但不刷新
            context_dict['msg1'] = form1.errors
            return render(request, 'datainput_ic_xzy.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

#录入IC卡-超声波数据
def datainput_ic_csb(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    MeterId = request.session.get("MeterId", "")
    context_dict['MeterId'] = MeterId
    MeterType = request.session.get("MeterType", "")
    context_dict['MeterType'] = MeterType
    ManufactureName_id = request.session.get("ManufactureName_id", "")
    TimeOfProduce = request.session.get("TimeOfProduce", "")
    if request.method == 'GET':
        form1 = Meter_ICForm()
        form2 = Meter_CSBForm()
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['msg1'] = ""
        context_dict['msg2'] = ""
        return render(request, 'datainput_ic_csb.html', context_dict)
    else:
        form1 = Meter_ICForm(request.POST)
        form2 = Meter_CSBForm(request.POST)
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        if form1.is_valid():
            if form2.is_valid():
                try:
                   subtime = datetime.datetime.now()
                   GS_MeterTypeInfo.objects.create(
                       MeterId=MeterId,
                       MeterType=MeterType,
                       ManufactureName_id=ManufactureName_id,
                       TimeOfProduce=TimeOfProduce,
                       Subtime=subtime,
                       user_id = reinfo[3]
                   )
                   meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                   GS_MeterInfo_IC.objects.create(MeterId=MeterId, MeterTypeId_id=meter.id,**form1.cleaned_data)
                   GS_MeterInfo_CSB.objects.create(MeterId=MeterId, MeterTypeId_id=meter.id,**form2.cleaned_data)
                   context_dict['success_input'] = 1  # 录入成功
                except IntegrityError:
                   context_dict['duplicate_input'] = 3  # 表号重复
            else:
                # 数据不符合要求,本页面回滚，但不刷新
                context_dict['msg2'] = form2.errors
                return render(request, 'datainput_ic_csb.html', context_dict)
        else:
            # 数据不符合要求,本页面回滚，但不刷新
            context_dict['msg1'] = form1.errors
            return render(request, 'datainput_ic_csb.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

#录入膜式表数据
def datainput_msb(request):
    context_dict={}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    MeterId = request.session.get("MeterId", "")
    context_dict['MeterId'] = MeterId
    MeterType = request.session.get("MeterType", "")
    context_dict['MeterType'] = MeterType
    ManufactureName_id = request.session.get("ManufactureName_id", "")
    TimeOfProduce = request.session.get("TimeOfProduce", "")
    if request.method == 'GET':
        form2 = Meter_MSBForm()
        context_dict['form2'] = form2
        return render(request, 'datainput_msb.html', context_dict)
    else:
        form2 = Meter_MSBForm(request.POST)
        context_dict['form2'] = form2
        if form2.is_valid():
            try:
                Subtime = datetime.datetime.now()
                GS_MeterTypeInfo.objects.create(
                    MeterId=MeterId,
                    MeterType=MeterType,
                    ManufactureName_id=ManufactureName_id,
                    TimeOfProduce=TimeOfProduce,
                    Subtime=Subtime,
                    user_id = reinfo[3]
                )
                meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                GS_MeterInfo_MSB.objects.create(MeterId=MeterId, MeterTypeId_id=meter.id, **form2.cleaned_data)
                context_dict['success_input'] = 1  # 录入成功
            except IntegrityError:
                context_dict['duplicate_input'] = 3  #表号重复
        else:
            #数据不符合要求,本页面回滚，但不刷新
            context_dict['msg2'] = form2.errors
            return render(request,'datainput_msb.html',context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

#录入修正仪数据
def datainput_xzy(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    MeterId = request.session.get("MeterId", "")
    context_dict['MeterId'] = MeterId
    MeterType = request.session.get("MeterType", "")
    context_dict['MeterType'] = MeterType
    ManufactureName_id = request.session.get("ManufactureName_id", "")
    TimeOfProduce = request.session.get("TimeOfProduce", "")
    if request.method == 'GET':
        form2 = Meter_XZYForm()
        context_dict['form2'] = form2
        return render(request, 'datainput_xzy.html', context_dict)
    else:
        form2 = Meter_XZYForm(request.POST)
        context_dict['form2'] = form2
        if form2.is_valid():
            try:
                subtime = datetime.datetime.now()
                GS_MeterTypeInfo.objects.create(
                    MeterId=MeterId,
                    MeterType=MeterType,
                    ManufactureName_id=ManufactureName_id,
                    TimeOfProduce=TimeOfProduce,
                    Subtime=subtime,
                    user_id = reinfo[3]
                )
                meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                GS_MeterInfo_XZY.objects.create(MeterId=MeterId,  MeterTypeId_id=meter.id,**form2.cleaned_data)
                context_dict['success_input'] = 1  # 录入成功
            except IntegrityError:
                context_dict['duplicate_input'] = 3  #表号重复
        else:
            #数据不符合要求,本页面回滚，但不刷新
            context_dict['msg2'] = form2.errors
            return render(request,'datainput_xzy.html',context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

#录入超声波数据
def datainput_csb(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    MeterId = request.session.get("MeterId", "")
    context_dict['MeterId'] = MeterId
    MeterType = request.session.get("MeterType", "")
    context_dict['MeterType'] = MeterType
    ManufactureName_id = request.session.get("ManufactureName_id", "")
    TimeOfProduce = request.session.get("TimeOfProduce", "")
    if request.method == 'GET':
        form2 = Meter_CSBForm()
        context_dict['form2'] = form2
        return render(request, 'datainput_csb.html', context_dict)
    else:
        form2 = Meter_CSBForm(request.POST)
        context_dict['form2'] = form2
        if form2.is_valid():
            try:
                subtime = datetime.datetime.now()
                GS_MeterTypeInfo.objects.create(
                    MeterId=MeterId,
                    MeterType=MeterType,
                    ManufactureName_id=ManufactureName_id,
                    TimeOfProduce=TimeOfProduce,
                    Subtime=subtime,
                    user_id = reinfo[3]
                )
                meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
                GS_MeterInfo_CSB.objects.create(MeterId=MeterId,  MeterTypeId_id=meter.id,**form2.cleaned_data)
                context_dict['success_input'] = 1  # 录入成功
            except IntegrityError:
                context_dict['duplicate_input'] = 3  # 表号重复
        else:
            # 数据不符合要求,本页面回滚，但不刷新
            context_dict['msg2'] = form2.errors
            return render(request, 'datainput_csb.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

#删除数据
def del_data(request):
    if request.method=="POST":
        MeterToDel = request.POST['MeterId']
        MeterType = request.POST['MeterType']
        #子表先删除，父表才能删除
        try:
            if MeterType == 'IC卡-膜式表':
               GS_MeterInfo_IC.objects.get(MeterId__exact=MeterToDel).delete()
               GS_MeterInfo_MSB.objects.get(MeterId__exact=MeterToDel).delete()
            if MeterType == "IC卡-修正仪":
                GS_MeterInfo_IC.objects.get(MeterId__exact=MeterToDel).delete()
                GS_MeterInfo_XZY.objects.get(MeterId__exact=MeterToDel).delete()
            if MeterType == "IC卡-超声波":
                GS_MeterInfo_IC.objects.get(MeterId__exact=MeterToDel).delete()
                GS_MeterInfo_CSB.objects.get(MeterId__exact=MeterToDel).delete()
            if MeterType == "膜式表":
                GS_MeterInfo_MSB.objects.get(MeterId__exact=MeterToDel).delete()
            if MeterType == "修正仪":
                GS_MeterInfo_XZY.objects.get(MeterId__exact=MeterToDel).delete()
            if MeterType == "超声波":
                GS_MeterInfo_CSB.objects.get(MeterId__exact=MeterToDel).delete()
            GS_MeterTypeInfo.objects.filter(MeterId__exact=MeterToDel).delete()  #父表
            return HttpResponse("1")
        except:
            return HttpResponse("2")

#修改数据
def edit_data(request):
    meterid = request.GET.get('MeterId')
    metertype = request.GET.get('MeterType')
    if metertype == 'IC卡-膜式表':
        url = '/edit_ic_msb/?p1=' + str(meterid) + '&p2=' + metertype
        return redirect(url)
    if metertype == "IC卡-修正仪":
        url = '/edit_ic_xzy/?p1=' + str(meterid) + '&p2=' + metertype
        return redirect(url)
    if metertype == "IC卡-超声波":
        url = '/edit_ic_csb/?p1=' + str(meterid) + '&p2=' + metertype
        return redirect(url)
    if metertype == "膜式表":
        url = '/edit_msb/?p1=' + str(meterid) + '&p2=' + metertype
        return redirect(url)
    if metertype == "修正仪":
        url = '/edit_xzy/?p1=' + str(meterid) + '&p2=' + metertype
        return redirect(url)
    if metertype == "超声波":
        url = '/edit_csb/?p1=' + str(meterid) + '&p2=' + metertype
        return redirect(url)

def edit_ic_msb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(id=id).values(
            'MeterId','MeterType','ManufactureName_id','TimeOfProduce',
        ).first()
        row1 = GS_MeterInfo_IC.objects.filter(MeterTypeId_id=id).values(
            'MeterId','ChargingStatusWord', 'CurrentVol', 'RemainingSum', 'CumulativeSum', 'CurrentPrice', 'CurrentPriceInitialVol',
            'LastPrice', 'LastPriceInitialVol', 'ChargingTime', 'VerComparison','PriceSysDate','PriceMode','PriceSysVer', 'PriceNormal',
            'PriceSysCycle', 'PriceCycleDate',  'PriceClearSign',  'PriceEndDateOne','PriceOne1', 'PriceOneAmount1','PriceOne2', 'PriceOneAmount2',
            'PriceOne3', 'PriceEndDateTwo', 'PriceTwo1', 'PriceTwoAmount1', 'PriceTwo2', 'PriceTwoAmount2','PriceTwo3', 'PriceEndDateThree', 'PriceThree1',
            'PriceThreeAmount1', 'PriceThree2', 'PriceThreeAmount2','PriceThree3','PriceEndDateFour','PriceFour1', 'PriceFourAmount1', 'PriceFour2',
            'PriceFourAmount2', 'PriceFour3', 'PriceEndDateFive','PriceFive1', 'PriceFiveAmount1', 'PriceFive2','PriceFiveAmount2', 'PriceFive3',
            'PriceSysDate_C', 'PriceSysCycle_C', 'PriceMode_C','PriceCycleDate_C', 'PriceSysVer_C', 'PriceClearSign_C',  'PriceNormal_C','DelayExists_C',
            'PriceEndDateOne_C', 'PriceOne1_C', 'PriceOneAmount1_C', 'PriceOne2_C', 'PriceOneAmount2_C', 'PriceOne3_C',
            'PriceEndDateTwo_C', 'PriceTwo1_C', 'PriceTwoAmount1_C', 'PriceTwo2_C', 'PriceTwoAmount2_C', 'PriceTwo3_C',
            'PriceEndDateThree_C', 'PriceThree1_C', 'PriceThreeAmount1_C', 'PriceThree2_C', 'PriceThreeAmount2_C', 'PriceThree3_C',
            'PriceEndDateFour_C', 'PriceFour1_C', 'PriceFourAmount1_C', 'PriceFour2_C', 'PriceFourAmount2_C', 'PriceFour3_C',
            'PriceEndDateFive_C', 'PriceFive1_C', 'PriceFiveAmount1_C', 'PriceFive2_C', 'PriceFiveAmount2_C', 'PriceFive3_C',
            'RechargeDate1','RemainingSumBefore1','RechargeSum1',
            'RechargeDate2','RemainingSumBefore2','RechargeSum2',
            'RechargeDate3', 'RemainingSumBefore3','RechargeSum3',
            'RechargeDate4','RemainingSumBefore4','RechargeSum4',
            'RechargeDate5', 'RemainingSumBefore5','RechargeSum5',
        ).first()
        row2 = GS_MeterInfo_MSB.objects.filter(MeterTypeId_id=id).values(
        'MeterId','Com_no_msb','Sw_rlse_msb','Real_vol','Meter_v','Temperature_msb','Status',
        'DropMeter1_msb','DropMeter2_msb','ReverseInstall1_msb','ReverseInstall2_msb','MeasureBreakdown1_msb',
        'MeasureBreakdown2_msb','TSensorBreakdown1_msb','TSensorBreakdown2_msb','PSensorBreakdown1_msb','PSensorBreakdown2_msb',
        'TrafficAbnormality1_msb','TrafficAbnormality2_msb','ComVol1_msb','ComVol2_msb','BaseVol1_msb','BaseVol2_msb',
        'CollectFault1_msb','CollectFault2_msb','GasLeakClose1_msb','GasLeakClose2_msb','GasStolenClose1_msb','GasStolenClose2_msb',
        'ResetClose1_msb','ResetClose2_msb','LowVolClose1_msb','LowVolClose2_msb','CollectClose1_msb','CollectClose2_msb','CommandClose1_msb',
        'CommandClose2_msb','ManulOpen1_msb','ManulOpen2_msb',
        'FTPUserName_msb', 'FTPPassword_msb', 'FTPAddress_msb', 'FTPCatalog_msb', 'FileName_msb',
        ).first()
        form1 = Meter_ICForm(initial=row1)  # 加上initial就不会自身校验了,data就有验证规则了
        form2 = Meter_MSBForm(initial=row2)
        form0 = MeterTypeForm(initial=row0)
        context_dict['id'] = id
        context_dict['metertype'] = metertype
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        context_dict['msg1'] = form1.errors
        context_dict['msg2'] = form2.errors
        context_dict['msg0'] = form0.errors
        return render(request, 'edit_ic_msb.html', context_dict)
    else:
        form1 = Meter_ICForm(request.POST)
        form2 = Meter_MSBForm(request.POST)
        form0 = MeterTypeForm(request.POST)
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        if form0.is_valid():
            if form1.is_valid():
                if form2.is_valid():
                   MeterId = form0.cleaned_data['MeterId']
                   subtime = datetime.datetime.now()
                   try:
                       GS_MeterTypeInfo.objects.filter(id=id).update(
                           Subtime=subtime,
                           IsSubmit=0,
                           IsDataChecked=0,
                           DataCheckedResult=0,
                           IsAllocated=0,
                           IsTest=0,
                           CommandTest=None,
                           ICTest=None,
                           ChuTest=None,
                           ZhoTest=None,
                           MianTest=None,
                           **form0.cleaned_data
                       )
                       GS_MeterInfo_IC.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId, **form1.cleaned_data)
                       GS_MeterInfo_MSB.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId, **form2.cleaned_data)
                       context_dict['success_edit'] = 1  # 修改成功
                   except:
                       context_dict['none_edit'] = 3  # 未找到该表号
                else:
                   # 修改失败，回滚本页面，错误信息可以显示出来
                    context_dict['msg2'] = form2.errors
                    return render(request, 'edit_ic_msb.html', context_dict)
            else:
                # 修改失败，回滚本页面，错误信息可以显示出来
                context_dict['msg0'] = form1.errors
                return render(request, 'edit_ic_msb.html', context_dict)
        else:
            # 修改失败，回滚本页面，错误信息可以显示出来
            context_dict['msg1'] = form1.errors
            return render(request, 'edit_ic_msb.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

def edit_ic_xzy(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(id=id).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row1 = GS_MeterInfo_IC.objects.filter(MeterTypeId_id=id).values(
            'MeterId', 'ChargingStatusWord', 'CurrentVol', 'RemainingSum', 'CumulativeSum', 'CurrentPrice',
            'CurrentPriceInitialVol',
            'LastPrice', 'LastPriceInitialVol', 'ChargingTime', 'VerComparison', 'PriceSysDate', 'PriceMode',
            'PriceSysVer', 'PriceNormal',
            'PriceSysCycle', 'PriceCycleDate', 'PriceClearSign', 'PriceEndDateOne', 'PriceOne1', 'PriceOneAmount1',
            'PriceOne2', 'PriceOneAmount2',
            'PriceOne3', 'PriceEndDateTwo', 'PriceTwo1', 'PriceTwoAmount1', 'PriceTwo2', 'PriceTwoAmount2', 'PriceTwo3',
            'PriceEndDateThree', 'PriceThree1',
            'PriceThreeAmount1', 'PriceThree2', 'PriceThreeAmount2', 'PriceThree3', 'PriceEndDateFour', 'PriceFour1',
            'PriceFourAmount1', 'PriceFour2',
            'PriceFourAmount2', 'PriceFour3', 'PriceEndDateFive', 'PriceFive1', 'PriceFiveAmount1', 'PriceFive2',
            'PriceFiveAmount2', 'PriceFive3',
            'PriceSysDate_C', 'PriceSysCycle_C', 'PriceMode_C', 'PriceCycleDate_C', 'PriceSysVer_C', 'PriceClearSign_C',
            'PriceNormal_C', 'DelayExists_C',
            'PriceEndDateOne_C', 'PriceOne1_C', 'PriceOneAmount1_C', 'PriceOne2_C', 'PriceOneAmount2_C', 'PriceOne3_C',
            'PriceEndDateTwo_C', 'PriceTwo1_C', 'PriceTwoAmount1_C', 'PriceTwo2_C', 'PriceTwoAmount2_C', 'PriceTwo3_C',
            'PriceEndDateThree_C', 'PriceThree1_C', 'PriceThreeAmount1_C', 'PriceThree2_C', 'PriceThreeAmount2_C',
            'PriceThree3_C',
            'PriceEndDateFour_C', 'PriceFour1_C', 'PriceFourAmount1_C', 'PriceFour2_C', 'PriceFourAmount2_C',
            'PriceFour3_C',
            'PriceEndDateFive_C', 'PriceFive1_C', 'PriceFiveAmount1_C', 'PriceFive2_C', 'PriceFiveAmount2_C',
            'PriceFive3_C',
            'RechargeDate1', 'RemainingSumBefore1', 'RechargeSum1',
            'RechargeDate2', 'RemainingSumBefore2', 'RechargeSum2',
            'RechargeDate3', 'RemainingSumBefore3', 'RechargeSum3',
            'RechargeDate4', 'RemainingSumBefore4', 'RechargeSum4',
            'RechargeDate5', 'RemainingSumBefore5', 'RechargeSum5',
        ).first()
        row2 = GS_MeterInfo_XZY.objects.filter(MeterTypeId_id=id).values(
        'MeterId','Com_no_xzy','Sw_rlse_xzy','MeterNum','Temperature_xzy','Disturb_Total_Vol',
        'Pressure','Correction_E','Stan_Total_Vol','Stan_Ins_Ele_xzy','Work_Total_Vol','Work_Ins_Ele_xzy',
        'DropMeter1_xzy', 'DropMeter2_xzy','ReverseInstall1_xzy','ReverseInstall2_xzy','MeasureBreakdown1_xzy',
        'MeasureBreakdown2_xzy','TSensorBreakdown1_xzy','TSensorBreakdown2_xzy','PSensorBreakdown1_xzy','PSensorBreakdown2_xzy',
        'TrafficAbnormality1_xzy','TrafficAbnormality2_xzy','ComVol1_xzy','ComVol2_xzy', 'BaseVol1_xzy','BaseVol2_xzy',
        'CollectFault1_xzy','CollectFault1_xzy',
        'GasLeakClose1_xzy','GasLeakClose2_xzy','GasStolenClose1_xzy','GasStolenClose2_xzy',
        'ResetClose1_xzy','ResetClose2_xzy','LowVolClose1_xzy','LowVolClose2_xzy','CollectClose1_xzy','CollectClose2_xzy','CommandClose1_xzy',
        'CommandClose2_xzy','ManulOpen1_xzy','ManulOpen2_xzy',
        'FTPUserName_xzy', 'FTPPassword_xzy', 'FTPAddress_xzy', 'FTPCatalog_xzy', 'FileName_xzy',
        ).first()
        form1 = Meter_ICForm(initial=row1)  # 加上initial就不会自身校验了,data就有验证规则了
        form2 = Meter_XZYForm(initial=row2)
        form0 = MeterTypeForm(initial=row0)
        context_dict['id'] = id
        context_dict['metertype'] = metertype
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        context_dict['msg1'] = form1.errors
        context_dict['msg2'] = form2.errors
        context_dict['msg0'] = form0.errors
        return render(request, 'edit_ic_xzy.html', context_dict)
    else:
        form1 = Meter_ICForm(request.POST)
        form2 = Meter_XZYForm(request.POST)
        form0 = MeterTypeForm(request.POST)
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        if form0.is_valid():
            if form1.is_valid():
                if form2.is_valid():
                    MeterId = form0.cleaned_data['MeterId']
                    subtime = datetime.datetime.now()
                    try:
                        GS_MeterTypeInfo.objects.filter(id=id).update(
                            Subtime=subtime,
                            IsSubmit=0,
                            IsDataChecked=0,
                            DataCheckedResult=0,
                            IsAllocated=0,
                            IsTest=0,
                            CommandTest=None,
                            ICTest=None,
                            ChuTest=None,
                            ZhoTest=None,
                            MianTest=None,
                            **form0.cleaned_data
                        )
                        GS_MeterInfo_IC.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form1.cleaned_data)
                        GS_MeterInfo_XZY.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form2.cleaned_data)
                        context_dict['success_edit'] = 1  # 修改成功
                    except:
                        context_dict['none_edit'] = 3  # 未找到该表号
                else:
                    # 修改失败，回滚本页面，错误信息可以显示出来
                    context_dict['msg2'] = form2.errors
                    return render(request, 'edit_ic_xzy.html', context_dict)
            else:
                # 修改失败，回滚本页面，错误信息可以显示出来
                context_dict['msg1'] = form1.errors
                return render(request, 'edit_ic_xzy.html', context_dict)
        else:
            # 修改失败，回滚本页面，错误信息可以显示出来
            context_dict['msg0'] = form0.errors
            return render(request, 'edit_ic_xzy.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

def edit_ic_csb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(id=id).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row1 = GS_MeterInfo_IC.objects.filter(MeterTypeId_id=id).values(
            'MeterId', 'ChargingStatusWord', 'CurrentVol', 'RemainingSum', 'CumulativeSum', 'CurrentPrice',
            'CurrentPriceInitialVol',
            'LastPrice', 'LastPriceInitialVol', 'ChargingTime', 'VerComparison', 'PriceSysDate', 'PriceMode',
            'PriceSysVer', 'PriceNormal',
            'PriceSysCycle', 'PriceCycleDate', 'PriceClearSign', 'PriceEndDateOne', 'PriceOne1', 'PriceOneAmount1',
            'PriceOne2', 'PriceOneAmount2',
            'PriceOne3', 'PriceEndDateTwo', 'PriceTwo1', 'PriceTwoAmount1', 'PriceTwo2', 'PriceTwoAmount2',
            'PriceTwo3', 'PriceEndDateThree', 'PriceThree1',
            'PriceThreeAmount1', 'PriceThree2', 'PriceThreeAmount2', 'PriceThree3', 'PriceEndDateFour',
            'PriceFour1', 'PriceFourAmount1', 'PriceFour2',
            'PriceFourAmount2', 'PriceFour3', 'PriceEndDateFive', 'PriceFive1', 'PriceFiveAmount1', 'PriceFive2',
            'PriceFiveAmount2', 'PriceFive3',
            'PriceSysDate_C', 'PriceSysCycle_C', 'PriceMode_C', 'PriceCycleDate_C', 'PriceSysVer_C',
            'PriceClearSign_C', 'PriceNormal_C', 'DelayExists_C',
            'PriceEndDateOne_C', 'PriceOne1_C', 'PriceOneAmount1_C', 'PriceOne2_C', 'PriceOneAmount2_C',
            'PriceOne3_C',
            'PriceEndDateTwo_C', 'PriceTwo1_C', 'PriceTwoAmount1_C', 'PriceTwo2_C', 'PriceTwoAmount2_C',
            'PriceTwo3_C',
            'PriceEndDateThree_C', 'PriceThree1_C', 'PriceThreeAmount1_C', 'PriceThree2_C', 'PriceThreeAmount2_C',
            'PriceThree3_C',
            'PriceEndDateFour_C', 'PriceFour1_C', 'PriceFourAmount1_C', 'PriceFour2_C', 'PriceFourAmount2_C',
            'PriceFour3_C',
            'PriceEndDateFive_C', 'PriceFive1_C', 'PriceFiveAmount1_C', 'PriceFive2_C', 'PriceFiveAmount2_C',
            'PriceFive3_C',
            'RechargeDate1', 'RemainingSumBefore1', 'RechargeSum1',
            'RechargeDate2', 'RemainingSumBefore2', 'RechargeSum2',
            'RechargeDate3', 'RemainingSumBefore3', 'RechargeSum3',
            'RechargeDate4', 'RemainingSumBefore4', 'RechargeSum4',
            'RechargeDate5', 'RemainingSumBefore5', 'RechargeSum5',
        ).first()
        row2 = GS_MeterInfo_CSB.objects.filter(MeterTypeId_id=id).values(
        'MeterId','Com_no_csb', 'Sw_rlse_csb', 'Vol1','Stan_Ins_Ele_csb','Vol2',
        'Work_Ins_Ele_csb','MeterStateWord', 'Temperature_csb', 'MeterInStateWord','PValue',
        'Stan_Total_Ele','Peak_Ele','Work_Total_Ele','DropMeter1_csb', 'DropMeter2_csb', 'ReverseInstall1_csb',
        'ReverseInstall2_csb','MeasureBreakdown1_csb', 'MeasureBreakdown2_csb','TSensorBreakdown1_csb','TSensorBreakdown2_csb',
        'PSensorBreakdown1_csb', 'PSensorBreakdown2_csb','TrafficAbnormality1_csb','TrafficAbnormality2_csb',
        'ComVol1_csb','ComVol2_csb','BaseVol1_csb','BaseVol2_csb','CollectFault1_csb','CollectFault1_csb',
        'GasLeakClose1_csb', 'GasLeakClose2_csb',
        'GasStolenClose1_csb','GasStolenClose2_csb',
        'ResetClose1_csb','ResetClose2_csb','LowVolClose1_csb','LowVolClose2_csb','CollectClose1_csb','CollectClose2_csb','CommandClose1_csb',
        'CommandClose2_csb','ManulOpen1_csb','ManulOpen2_csb',
        'AF_ULimit1','AF_DLimit1','AF_LLimit1','AF_ULimit2','AF_DLimit2',
        'AF_LLimit2','AF_ULimit3','AF_DLimit3','AF_LLimit3',
        'FTPUserName_csb', 'FTPPassword_csb', 'FTPAddress_csb', 'FTPCatalog_csb', 'FileName_csb',
        ).first()
        form1 = Meter_ICForm(initial=row1)  # 加上initial就不会自身校验了,data就有验证规则了
        form2 = Meter_CSBForm(initial=row2)
        form0 = MeterTypeForm(initial=row0)
        context_dict['id'] = id
        context_dict['metertype'] = metertype
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        context_dict['msg1'] = form1.errors
        context_dict['msg2'] = form2.errors
        context_dict['msg0'] = form0.errors
        return render(request, 'edit_ic_csb.html', context_dict)
    else:
        form1 = Meter_ICForm(request.POST)
        form2 = Meter_CSBForm(request.POST)
        form0 = MeterTypeForm(request.POST)
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        if form0.is_valid():
            if form1.is_valid():
                if form2.is_valid():
                    MeterId = form0.cleaned_data['MeterId']
                    subtime = datetime.datetime.now()
                    try:
                        GS_MeterTypeInfo.objects.filter(id=id).update(
                            Subtime=subtime,
                            IsSubmit=0,
                            IsDataChecked=0,
                            DataCheckedResult=0,
                            IsAllocated=0,
                            IsTest=0,
                            CommandTest=None,
                            ICTest=None,
                            ChuTest=None,
                            ZhoTest=None,
                            MianTest=None,
                            **form0.cleaned_data
                        )
                        GS_MeterInfo_IC.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form1.cleaned_data)
                        GS_MeterInfo_CSB.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form2.cleaned_data)
                        context_dict['success_edit'] = 1  # 修改成功
                    except:
                        context_dict['none_edit'] = 3  # 未找到该表号
                else:
                    # 修改失败，回滚本页面，错误信息可以显示出来
                    context_dict['msg2'] = form2.errors
                    return render(request, 'edit_ic_csb.html', context_dict)
            else:
                # 修改失败，回滚本页面，错误信息可以显示出来
                context_dict['msg1'] = form1.errors
                return render(request, 'edit_ic_csb.html', context_dict)
        else:
            # 修改失败，回滚本页面，错误信息可以显示出来
            context_dict['msg0'] = form0.errors
            return render(request, 'edit_ic_csb.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

def edit_msb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(id=id).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row2 = GS_MeterInfo_MSB.objects.filter(MeterTypeId_id=id).values(
            'MeterId', 'Com_no_msb', 'Sw_rlse_msb', 'Real_vol', 'Meter_v', 'Temperature_msb', 'Status',
            'DropMeter1_msb', 'DropMeter2_msb', 'ReverseInstall1_msb', 'ReverseInstall2_msb', 'MeasureBreakdown1_msb',
            'MeasureBreakdown2_msb', 'TSensorBreakdown1_msb', 'TSensorBreakdown2_msb', 'PSensorBreakdown1_msb',
            'PSensorBreakdown2_msb',
            'TrafficAbnormality1_msb', 'TrafficAbnormality2_msb', 'ComVol1_msb', 'ComVol2_msb', 'BaseVol1_msb',
            'BaseVol2_msb',
            'CollectFault1_msb', 'CollectFault2_msb', 'GasLeakClose1_msb', 'GasLeakClose2_msb', 'GasStolenClose1_msb',
            'GasStolenClose2_msb',
            'ResetClose1_msb', 'ResetClose2_msb', 'LowVolClose1_msb', 'LowVolClose2_msb', 'CollectClose1_msb',
            'CollectClose2_msb', 'CommandClose1_msb',
            'CommandClose2_msb', 'ManulOpen1_msb', 'ManulOpen2_msb',
            'FTPUserName_msb','FTPPassword_msb','FTPAddress_msb','FTPCatalog_msb','FileName_msb',
        ).first()
        form2 = Meter_MSBForm(initial=row2)
        form0 = MeterTypeForm(initial=row0)
        context_dict['id'] = id
        context_dict['metertype'] = metertype
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        context_dict['msg2'] = form2.errors
        context_dict['msg0'] = form0.errors
        return render(request, 'edit_msb.html', context_dict)
    else:
        form2 = Meter_MSBForm(request.POST)
        form0 = MeterTypeForm(request.POST)
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        if form0.is_valid():
            if form2.is_valid():
                MeterId = form0.cleaned_data['MeterId']
                subtime = datetime.datetime.now()
                try:
                    GS_MeterTypeInfo.objects.filter(id=id).update(
                        Subtime=subtime,
                        IsSubmit=0,
                        IsDataChecked=0,
                        DataCheckedResult=0,
                        IsAllocated=0,
                        IsTest=0,
                        CommandTest=None,
                        ICTest=None,
                        ChuTest=None,
                        ZhoTest=None,
                        MianTest=None,
                        **form0.cleaned_data
                    )
                    GS_MeterInfo_MSB.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form2.cleaned_data)
                    context_dict['success_edit'] = 1  #修改成功
                except:
                    context_dict['none_edit'] = 3  # 未找到该表号
            else:
                #修改失败，回滚本页面，错误信息可以显示出来
                context_dict['msg2'] = form2.errors
                return render(request, 'edit_msb.html', context_dict)
        else:
            # 修改失败，回滚本页面，错误信息可以显示出来
            context_dict['msg0'] = form0.errors
            return render(request, 'edit_msb.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

def edit_xzy(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(id=id).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row2 = GS_MeterInfo_XZY.objects.filter(MeterTypeId_id=id).values(
            'MeterId', 'Com_no_xzy', 'Sw_rlse_xzy', 'MeterNum', 'Temperature_xzy', 'Disturb_Total_Vol',
            'Pressure', 'Correction_E', 'Stan_Total_Vol', 'Stan_Ins_Ele_xzy', 'Work_Total_Vol', 'Work_Ins_Ele_xzy',
            'DropMeter1_xzy', 'DropMeter2_xzy', 'ReverseInstall1_xzy', 'ReverseInstall2_xzy', 'MeasureBreakdown1_xzy',
            'MeasureBreakdown2_xzy', 'TSensorBreakdown1_xzy', 'TSensorBreakdown2_xzy', 'PSensorBreakdown1_xzy',
            'PSensorBreakdown2_xzy',
            'TrafficAbnormality1_xzy', 'TrafficAbnormality2_xzy', 'ComVol1_xzy', 'ComVol2_xzy', 'BaseVol1_xzy',
            'BaseVol2_xzy',
            'CollectFault1_xzy', 'CollectFault1_xzy',
            'GasLeakClose1_xzy', 'GasLeakClose2_xzy', 'GasStolenClose1_xzy', 'GasStolenClose2_xzy',
             'ResetClose1_xzy', 'ResetClose2_xzy', 'LowVolClose1_xzy', 'LowVolClose2_xzy',
            'CollectClose1_xzy', 'CollectClose2_xzy', 'CommandClose1_xzy',
            'CommandClose2_xzy', 'ManulOpen1_xzy', 'ManulOpen2_xzy',
            'FTPUserName_xzy', 'FTPPassword_xzy', 'FTPAddress_xzy', 'FTPCatalog_xzy', 'FileName_xzy',
        ).first()
        form2 = Meter_XZYForm(initial=row2)
        form0 = MeterTypeForm(initial=row0)
        context_dict['id'] = id
        context_dict['metertype'] = metertype
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        context_dict['msg2'] = form2.errors
        context_dict['msg0'] = form0.errors
        return render(request, 'edit_xzy.html', context_dict)
    else:
        form2 = Meter_XZYForm(request.POST)
        form0 = MeterTypeForm(request.POST)
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        if form0.is_valid():
            if form2.is_valid():
                MeterId = form0.cleaned_data['MeterId']
                subtime = datetime.datetime.now()
                try:
                    GS_MeterTypeInfo.objects.filter(id=id).update(
                        Subtime=subtime,
                        IsSubmit=0,
                        IsDataChecked=0,
                        DataCheckedResult=0,
                        IsAllocated=0,
                        IsTest=0,
                        CommandTest=None,
                        ICTest=None,
                        ChuTest=None,
                        ZhoTest=None,
                        MianTest=None,
                        **form0.cleaned_data
                    )
                    GS_MeterInfo_XZY.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form2.cleaned_data)
                    context_dict['success_edit'] = 1  # 修改成功
                except:
                    context_dict['none_edit'] = 3  # 未找到该表号
            else:
                # 修改失败，回滚本页面，错误信息可以显示出来
                context_dict['msg2'] = form2.errors
                return render(request, 'edit_xzy.html', context_dict)
        else:
            # 修改失败，回滚本页面，错误信息可以显示出来
            context_dict['msg0'] = form0.errors
            return render(request, 'edit_xzy.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

def edit_csb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    id = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(id=id).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row2 = GS_MeterInfo_CSB.objects.filter(MeterTypeId_id=id).values(
            'MeterId', 'Com_no_csb', 'Sw_rlse_csb', 'Vol1', 'Stan_Ins_Ele_csb', 'Vol2',
            'Work_Ins_Ele_csb', 'MeterStateWord', 'Temperature_csb', 'MeterInStateWord', 'PValue',
            'Stan_Total_Ele', 'Peak_Ele', 'Work_Total_Ele', 'DropMeter1_csb', 'DropMeter2_csb', 'ReverseInstall1_csb',
            'ReverseInstall2_csb', 'MeasureBreakdown1_csb', 'MeasureBreakdown2_csb', 'TSensorBreakdown1_csb',
            'TSensorBreakdown2_csb',
            'PSensorBreakdown1_csb', 'PSensorBreakdown2_csb', 'TrafficAbnormality1_csb', 'TrafficAbnormality2_csb',
            'ComVol1_csb', 'ComVol2_csb', 'BaseVol1_csb', 'BaseVol2_csb', 'CollectFault1_csb', 'CollectFault1_csb',
            'GasLeakClose1_csb', 'GasLeakClose2_csb',
            'GasStolenClose1_csb', 'GasStolenClose2_csb',
            'ResetClose1_csb', 'ResetClose2_csb', 'LowVolClose1_csb', 'LowVolClose2_csb', 'CollectClose1_csb',
            'CollectClose2_csb', 'CommandClose1_csb',
            'CommandClose2_csb', 'ManulOpen1_csb', 'ManulOpen2_csb',
            'AF_ULimit1', 'AF_DLimit1', 'AF_LLimit1', 'AF_ULimit2', 'AF_DLimit2',
            'AF_LLimit2', 'AF_ULimit3', 'AF_DLimit3', 'AF_LLimit3',
            'FTPUserName_csb', 'FTPPassword_csb', 'FTPAddress_csb', 'FTPCatalog_csb', 'FileName_csb',
        ).first()
        form2 = Meter_CSBForm(initial=row2)
        form0 = MeterTypeForm(initial=row0)
        context_dict['id'] = id
        context_dict['metertype'] = metertype
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        context_dict['msg2'] = form2.errors
        context_dict['msg0'] = form0.errors
        return render(request, 'edit_csb.html', context_dict)
    else:
        form2 = Meter_CSBForm(request.POST)
        form0 = MeterTypeForm(request.POST)
        context_dict['form2'] = form2
        context_dict['form0'] = form0
        if form0.is_valid():
            if form2.is_valid():
                MeterId = form0.cleaned_data['MeterId']
                subtime = datetime.datetime.now()
                try:
                    GS_MeterTypeInfo.objects.filter(id=id).update(
                        Subtime=subtime,
                        IsSubmit=0,
                        IsDataChecked=0,
                        DataCheckedResult=0,
                        IsAllocated=0,
                        IsTest=0,
                        CommandTest=None,
                        ICTest=None,
                        ChuTest=None,
                        ZhoTest=None,
                        MianTest=None,
                        **form0.cleaned_data
                    )
                    GS_MeterInfo_CSB.objects.filter(MeterTypeId_id=id).update(MeterId=MeterId,**form2.cleaned_data)
                    context_dict['success_edit'] = 1  # 修改成功
                except:
                    context_dict['none_edit'] = 3  # 未找到该表号
            else:
                # 修改失败，回滚本页面，错误信息可以显示出来
                context_dict['msg2'] = form2.errors
                return render(request, 'edit_csb.html', context_dict)
        else:
            # 修改失败，回滚本页面，错误信息可以显示出来
            context_dict['msg0'] = form0.errors
            return render(request, 'edit_csb.html', context_dict)
        return render(request, 'sub-edit-check-result.html', context_dict)

#数据审核：显示待审核的所有燃气表
def datacheck(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    search_dict = dict()
    if request.method == 'GET':
        q_form = MeterQueryForm3()
        context_dict['q_form'] = q_form
        # 分页
        all_count = GS_MeterTypeInfo.objects.filter(IsSubmit=1,IsDataChecked=0).count()
        current_page = request.GET.get('page')
        page_info = PageInfo(current_page, all_count, 10, '/datacheck/', 11)
        meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=1,IsDataChecked=0)[page_info.start():page_info.end()]
        context_dict['meter_list'] = meter_list
        context_dict['page_info'] = page_info  # 不要忘了传到前端
        return render(request, 'datacheck.html',context_dict)
    else:
        q_form = MeterQueryForm3(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            manu = q_form.cleaned_data['ManufactureName_id']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if manu:
                search_dict['ManufactureName_id'] = manu
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            info = GS_MeterTypeInfo.objects.filter(IsSubmit=1, IsDataChecked=0,**search_dict)
            context_dict['meter_list'] = info
            return render(request, 'datacheck.html', context_dict)
        else:
            q_form = MeterQueryForm3()
            return HttpResponse("not found 404")

#审核数据根据表类型跳转
def check_data(request):
    look1 = request.GET.get('p1')
    request.session['look1'] = look1
    look2 = request.GET.get('p2')
    request.session['look2'] = look2
    MeterId = request.GET.get('MeterId')
    MeterType = request.GET.get('MeterType')
    if request.method =='GET':
        if MeterType == 'IC卡-膜式表':
            url = '/check_ic_msb/?p1=' + str(MeterId) + '&p2=' + MeterType
            return redirect(url)
        if MeterType == "IC卡-修正仪":
            url = '/check_ic_xzy/?p1=' + str(MeterId) + '&p2=' + MeterType
            return redirect(url)
        if MeterType == "IC卡-超声波":
            url = '/check_ic_csb/?p1=' + str(MeterId) + '&p2=' + MeterType
            return redirect(url)
        if MeterType == "膜式表":
            url = '/check_msb/?p1=' + str(MeterId) + '&p2=' + MeterType
            return redirect(url)
        if MeterType == "修正仪":
            url = '/check_xzy/?p1=' + str(MeterId) + '&p2=' + MeterType
            return redirect(url)
        if MeterType == "超声波":
            url = '/check_csb/?p1=' + str(MeterId) + '&p2=' + MeterType
            return redirect(url)

#显示IC卡-膜式表数据
def check_ic_msb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    look1 = request.session.get('look1','')
    context_dict['look1'] = look1
    look2 = request.session.get('look2', '')
    context_dict['look2'] = look2
    meterid = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(MeterId=meterid).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row1 = GS_MeterInfo_IC.objects.filter(MeterId=meterid).values(
            'MeterId', 'ChargingStatusWord', 'CurrentVol', 'RemainingSum', 'CumulativeSum', 'CurrentPrice',
            'CurrentPriceInitialVol',
            'LastPrice', 'LastPriceInitialVol', 'ChargingTime', 'VerComparison', 'PriceSysDate', 'PriceMode',
            'PriceSysVer', 'PriceNormal',
            'PriceSysCycle', 'PriceCycleDate', 'PriceClearSign', 'PriceEndDateOne', 'PriceOne1', 'PriceOneAmount1',
            'PriceOne2', 'PriceOneAmount2',
            'PriceOne3', 'PriceEndDateTwo', 'PriceTwo1', 'PriceTwoAmount1', 'PriceTwo2', 'PriceTwoAmount2', 'PriceTwo3',
            'PriceEndDateThree', 'PriceThree1',
            'PriceThreeAmount1', 'PriceThree2', 'PriceThreeAmount2', 'PriceThree3', 'PriceEndDateFour', 'PriceFour1',
            'PriceFourAmount1', 'PriceFour2',
            'PriceFourAmount2', 'PriceFour3', 'PriceEndDateFive', 'PriceFive1', 'PriceFiveAmount1', 'PriceFive2',
            'PriceFiveAmount2', 'PriceFive3',
            'PriceSysDate_C', 'PriceSysCycle_C', 'PriceMode_C', 'PriceCycleDate_C', 'PriceSysVer_C', 'PriceClearSign_C',
            'PriceNormal_C', 'DelayExists_C',
            'PriceEndDateOne_C', 'PriceOne1_C', 'PriceOneAmount1_C', 'PriceOne2_C', 'PriceOneAmount2_C', 'PriceOne3_C',
            'PriceEndDateTwo_C', 'PriceTwo1_C', 'PriceTwoAmount1_C', 'PriceTwo2_C', 'PriceTwoAmount2_C', 'PriceTwo3_C',
            'PriceEndDateThree_C', 'PriceThree1_C', 'PriceThreeAmount1_C', 'PriceThree2_C', 'PriceThreeAmount2_C',
            'PriceThree3_C',
            'PriceEndDateFour_C', 'PriceFour1_C', 'PriceFourAmount1_C', 'PriceFour2_C', 'PriceFourAmount2_C',
            'PriceFour3_C',
            'PriceEndDateFive_C', 'PriceFive1_C', 'PriceFiveAmount1_C', 'PriceFive2_C', 'PriceFiveAmount2_C',
            'PriceFive3_C',
            'RechargeDate1', 'RemainingSumBefore1', 'RechargeSum1',
            'RechargeDate2', 'RemainingSumBefore2', 'RechargeSum2',
            'RechargeDate3', 'RemainingSumBefore3', 'RechargeSum3',
            'RechargeDate4', 'RemainingSumBefore4', 'RechargeSum4',
            'RechargeDate5', 'RemainingSumBefore5', 'RechargeSum5',
        ).first()
        row2 = GS_MeterInfo_MSB.objects.filter(MeterId=meterid).values(
            'MeterId', 'Com_no_msb', 'Sw_rlse_msb', 'Real_vol', 'Meter_v', 'Temperature_msb', 'Status',
            'DropMeter1_msb', 'DropMeter2_msb', 'ReverseInstall1_msb', 'ReverseInstall2_msb', 'MeasureBreakdown1_msb',
            'MeasureBreakdown2_msb', 'TSensorBreakdown1_msb', 'TSensorBreakdown2_msb', 'PSensorBreakdown1_msb',
            'PSensorBreakdown2_msb',
            'TrafficAbnormality1_msb', 'TrafficAbnormality2_msb', 'ComVol1_msb', 'ComVol2_msb', 'BaseVol1_msb',
            'BaseVol2_msb',
            'CollectFault1_msb', 'CollectFault2_msb', 'GasLeakClose1_msb', 'GasLeakClose2_msb', 'GasStolenClose1_msb',
            'GasStolenClose2_msb',
            'ResetClose1_msb', 'ResetClose2_msb', 'LowVolClose1_msb', 'LowVolClose2_msb', 'CollectClose1_msb',
            'CollectClose2_msb', 'CommandClose1_msb',
            'CommandClose2_msb', 'ManulOpen1_msb', 'ManulOpen2_msb',
            'FTPUserName_msb', 'FTPPassword_msb', 'FTPAddress_msb', 'FTPCatalog_msb', 'FileName_msb',
        ).first()
        form0 = MeterTypeForm(initial=row0)
        form1 = Meter_ICForm(initial=row1)  # 加上initial就不会自身校验了,data就有验证规则了
        form2 = Meter_MSBForm(initial=row2)
        context_dict['meterid'] = meterid
        context_dict['metertype'] = metertype
        context_dict['form0'] = form0
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['msg0'] = form0.errors
        context_dict['msg1'] = form1.errors
        context_dict['msg2'] = form2.errors
        return render(request, 'check_ic_msb.html', context_dict)

#显示IC卡-修正仪数据
def check_ic_xzy(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    look1 = request.session.get('look1', '')
    context_dict['look1'] = look1
    look2 = request.session.get('look2', '')
    context_dict['look2'] = look2
    meterid = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(MeterId=meterid).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row1 = GS_MeterInfo_IC.objects.filter(MeterId=meterid).values(
            'MeterId', 'ChargingStatusWord', 'CurrentVol', 'RemainingSum', 'CumulativeSum', 'CurrentPrice',
            'CurrentPriceInitialVol',
            'LastPrice', 'LastPriceInitialVol', 'ChargingTime', 'VerComparison', 'PriceSysDate', 'PriceMode',
            'PriceSysVer', 'PriceNormal',
            'PriceSysCycle', 'PriceCycleDate', 'PriceClearSign', 'PriceEndDateOne', 'PriceOne1', 'PriceOneAmount1',
            'PriceOne2', 'PriceOneAmount2',
            'PriceOne3', 'PriceEndDateTwo', 'PriceTwo1', 'PriceTwoAmount1', 'PriceTwo2', 'PriceTwoAmount2', 'PriceTwo3',
            'PriceEndDateThree', 'PriceThree1',
            'PriceThreeAmount1', 'PriceThree2', 'PriceThreeAmount2', 'PriceThree3', 'PriceEndDateFour', 'PriceFour1',
            'PriceFourAmount1', 'PriceFour2',
            'PriceFourAmount2', 'PriceFour3', 'PriceEndDateFive', 'PriceFive1', 'PriceFiveAmount1', 'PriceFive2',
            'PriceFiveAmount2', 'PriceFive3',
            'PriceSysDate_C', 'PriceSysCycle_C', 'PriceMode_C', 'PriceCycleDate_C', 'PriceSysVer_C', 'PriceClearSign_C',
            'PriceNormal_C', 'DelayExists_C',
            'PriceEndDateOne_C', 'PriceOne1_C', 'PriceOneAmount1_C', 'PriceOne2_C', 'PriceOneAmount2_C', 'PriceOne3_C',
            'PriceEndDateTwo_C', 'PriceTwo1_C', 'PriceTwoAmount1_C', 'PriceTwo2_C', 'PriceTwoAmount2_C', 'PriceTwo3_C',
            'PriceEndDateThree_C', 'PriceThree1_C', 'PriceThreeAmount1_C', 'PriceThree2_C', 'PriceThreeAmount2_C',
            'PriceThree3_C',
            'PriceEndDateFour_C', 'PriceFour1_C', 'PriceFourAmount1_C', 'PriceFour2_C', 'PriceFourAmount2_C',
            'PriceFour3_C',
            'PriceEndDateFive_C', 'PriceFive1_C', 'PriceFiveAmount1_C', 'PriceFive2_C', 'PriceFiveAmount2_C',
            'PriceFive3_C',
            'RechargeDate1', 'RemainingSumBefore1', 'RechargeSum1',
            'RechargeDate2', 'RemainingSumBefore2', 'RechargeSum2',
            'RechargeDate3', 'RemainingSumBefore3', 'RechargeSum3',
            'RechargeDate4', 'RemainingSumBefore4', 'RechargeSum4',
            'RechargeDate5', 'RemainingSumBefore5', 'RechargeSum5',
        ).first()
        row2 = GS_MeterInfo_XZY.objects.filter(MeterId=meterid).values(
            'MeterId', 'Com_no_xzy', 'Sw_rlse_xzy', 'MeterNum', 'Temperature_xzy', 'Disturb_Total_Vol',
            'Pressure', 'Correction_E', 'Stan_Total_Vol', 'Stan_Ins_Ele_xzy', 'Work_Total_Vol', 'Work_Ins_Ele_xzy',
            'DropMeter1_xzy', 'DropMeter2_xzy', 'ReverseInstall1_xzy', 'ReverseInstall2_xzy', 'MeasureBreakdown1_xzy',
            'MeasureBreakdown2_xzy', 'TSensorBreakdown1_xzy', 'TSensorBreakdown2_xzy', 'PSensorBreakdown1_xzy',
            'PSensorBreakdown2_xzy',
            'TrafficAbnormality1_xzy', 'TrafficAbnormality2_xzy', 'ComVol1_xzy', 'ComVol2_xzy', 'BaseVol1_xzy',
            'BaseVol2_xzy',
            'CollectFault1_xzy', 'CollectFault1_xzy',
            'GasLeakClose1_xzy', 'GasLeakClose2_xzy', 'GasStolenClose1_xzy', 'GasStolenClose2_xzy',
            'ResetClose1_xzy', 'ResetClose2_xzy', 'LowVolClose1_xzy', 'LowVolClose2_xzy',
            'CollectClose1_xzy', 'CollectClose2_xzy', 'CommandClose1_xzy',
            'CommandClose2_xzy', 'ManulOpen1_xzy', 'ManulOpen2_xzy',
            'FTPUserName_xzy', 'FTPPassword_xzy', 'FTPAddress_xzy', 'FTPCatalog_xzy', 'FileName_xzy',
        ).first()
        form0 = MeterTypeForm(initial=row0)
        form1 = Meter_ICForm(initial=row1)  # 加上initial就不会自身校验了,data就有验证规则了
        form2 = Meter_XZYForm(initial=row2)
        context_dict['meterid'] = meterid
        context_dict['metertype'] = metertype
        context_dict['form0'] = form0
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['msg0'] = form0.errors
        context_dict['msg1'] = form1.errors
        context_dict['msg2'] = form2.errors
        return render(request, 'check_ic_xzy.html', context_dict)

#显示IC卡-超声波数据
def check_ic_csb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    look1 = request.session.get('look1', '')
    context_dict['look1'] = look1
    look2 = request.session.get('look2', '')
    context_dict['look2'] = look2
    meterid = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(MeterId=meterid).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row1 = GS_MeterInfo_IC.objects.filter(MeterId=meterid).values(
            'MeterId', 'ChargingStatusWord', 'CurrentVol', 'RemainingSum', 'CumulativeSum', 'CurrentPrice',
            'CurrentPriceInitialVol',
            'LastPrice', 'LastPriceInitialVol', 'ChargingTime', 'VerComparison', 'PriceSysDate', 'PriceMode',
            'PriceSysVer', 'PriceNormal',
            'PriceSysCycle', 'PriceCycleDate', 'PriceClearSign', 'PriceEndDateOne', 'PriceOne1', 'PriceOneAmount1',
            'PriceOne2', 'PriceOneAmount2',
            'PriceOne3', 'PriceEndDateTwo', 'PriceTwo1', 'PriceTwoAmount1', 'PriceTwo2', 'PriceTwoAmount2',
            'PriceTwo3', 'PriceEndDateThree', 'PriceThree1',
            'PriceThreeAmount1', 'PriceThree2', 'PriceThreeAmount2', 'PriceThree3', 'PriceEndDateFour',
            'PriceFour1', 'PriceFourAmount1', 'PriceFour2',
            'PriceFourAmount2', 'PriceFour3', 'PriceEndDateFive', 'PriceFive1', 'PriceFiveAmount1', 'PriceFive2',
            'PriceFiveAmount2', 'PriceFive3',
            'PriceSysDate_C', 'PriceSysCycle_C', 'PriceMode_C', 'PriceCycleDate_C', 'PriceSysVer_C',
            'PriceClearSign_C', 'PriceNormal_C', 'DelayExists_C',
            'PriceEndDateOne_C', 'PriceOne1_C', 'PriceOneAmount1_C', 'PriceOne2_C', 'PriceOneAmount2_C',
            'PriceOne3_C',
            'PriceEndDateTwo_C', 'PriceTwo1_C', 'PriceTwoAmount1_C', 'PriceTwo2_C', 'PriceTwoAmount2_C',
            'PriceTwo3_C',
            'PriceEndDateThree_C', 'PriceThree1_C', 'PriceThreeAmount1_C', 'PriceThree2_C', 'PriceThreeAmount2_C',
            'PriceThree3_C',
            'PriceEndDateFour_C', 'PriceFour1_C', 'PriceFourAmount1_C', 'PriceFour2_C', 'PriceFourAmount2_C',
            'PriceFour3_C',
            'PriceEndDateFive_C', 'PriceFive1_C', 'PriceFiveAmount1_C', 'PriceFive2_C', 'PriceFiveAmount2_C',
            'PriceFive3_C',
            'RechargeDate1', 'RemainingSumBefore1', 'RechargeSum1',
            'RechargeDate2', 'RemainingSumBefore2', 'RechargeSum2',
            'RechargeDate3', 'RemainingSumBefore3', 'RechargeSum3',
            'RechargeDate4', 'RemainingSumBefore4', 'RechargeSum4',
            'RechargeDate5', 'RemainingSumBefore5', 'RechargeSum5',
        ).first()
        row2 = GS_MeterInfo_CSB.objects.filter(MeterId=meterid).values(
             'MeterId', 'Com_no_csb', 'Sw_rlse_csb', 'Vol1', 'Stan_Ins_Ele_csb', 'Vol2',
            'Work_Ins_Ele_csb', 'MeterStateWord', 'Temperature_csb', 'MeterInStateWord', 'PValue',
            'Stan_Total_Ele', 'Peak_Ele', 'Work_Total_Ele', 'DropMeter1_csb', 'DropMeter2_csb', 'ReverseInstall1_csb',
            'ReverseInstall2_csb', 'MeasureBreakdown1_csb', 'MeasureBreakdown2_csb', 'TSensorBreakdown1_csb',
            'TSensorBreakdown2_csb',
            'PSensorBreakdown1_csb', 'PSensorBreakdown2_csb', 'TrafficAbnormality1_csb', 'TrafficAbnormality2_csb',
            'ComVol1_csb', 'ComVol2_csb', 'BaseVol1_csb', 'BaseVol2_csb', 'CollectFault1_csb', 'CollectFault1_csb',
            'GasLeakClose1_csb', 'GasLeakClose2_csb',
            'GasStolenClose1_csb', 'GasStolenClose2_csb',
            'ResetClose1_csb', 'ResetClose2_csb', 'LowVolClose1_csb', 'LowVolClose2_csb', 'CollectClose1_csb',
            'CollectClose2_csb', 'CommandClose1_csb',
            'CommandClose2_csb', 'ManulOpen1_csb', 'ManulOpen2_csb',
            'AF_ULimit1', 'AF_DLimit1', 'AF_LLimit1', 'AF_ULimit2', 'AF_DLimit2',
            'AF_LLimit2', 'AF_ULimit3', 'AF_DLimit3', 'AF_LLimit3',
            'FTPUserName_csb', 'FTPPassword_csb', 'FTPAddress_csb', 'FTPCatalog_csb', 'FileName_csb',
        ).first()
        form0 = MeterTypeForm(initial=row0)
        form1 = Meter_ICForm(initial=row1)  # 加上initial就不会自身校验了,data就有验证规则了
        form2 = Meter_CSBForm(initial=row2)
        context_dict['form0'] = form0
        context_dict['meterid'] = meterid
        context_dict['metertype'] = metertype
        context_dict['form1'] = form1
        context_dict['form2'] = form2
        context_dict['msg0'] = form0.errors
        context_dict['msg1'] = form1.errors
        context_dict['msg2'] = form2.errors
        return render(request, 'check_ic_csb.html', context_dict)

def check_msb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    look1 = request.session.get('look1', '')
    context_dict['look1'] = look1
    look2 = request.session.get('look2', '')
    context_dict['look2'] = look2
    meterid = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(MeterId=meterid).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row2 = GS_MeterInfo_MSB.objects.filter(MeterId=meterid).values(
            'MeterId', 'Com_no_msb', 'Sw_rlse_msb', 'Real_vol', 'Meter_v', 'Temperature_msb', 'Status',
            'DropMeter1_msb', 'DropMeter2_msb', 'ReverseInstall1_msb', 'ReverseInstall2_msb', 'MeasureBreakdown1_msb',
            'MeasureBreakdown2_msb', 'TSensorBreakdown1_msb', 'TSensorBreakdown2_msb', 'PSensorBreakdown1_msb',
            'PSensorBreakdown2_msb',
            'TrafficAbnormality1_msb', 'TrafficAbnormality2_msb', 'ComVol1_msb', 'ComVol2_msb', 'BaseVol1_msb',
            'BaseVol2_msb',
            'CollectFault1_msb', 'CollectFault2_msb', 'GasLeakClose1_msb', 'GasLeakClose2_msb', 'GasStolenClose1_msb',
            'GasStolenClose2_msb',
            'ResetClose1_msb', 'ResetClose2_msb', 'LowVolClose1_msb', 'LowVolClose2_msb', 'CollectClose1_msb',
            'CollectClose2_msb', 'CommandClose1_msb',
            'CommandClose2_msb', 'ManulOpen1_msb', 'ManulOpen2_msb',
            'FTPUserName_msb', 'FTPPassword_msb', 'FTPAddress_msb', 'FTPCatalog_msb', 'FileName_msb',
        ).first()
        form0 = MeterTypeForm(initial=row0)
        form2 = Meter_MSBForm(initial=row2)
        context_dict['meterid'] = meterid
        context_dict['metertype'] = metertype
        context_dict['form0'] = form0
        context_dict['form2'] = form2
        context_dict['msg0'] = form0.errors
        context_dict['msg2'] = form2.errors
        return render(request, 'check_msb.html', context_dict)

def check_xzy(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    look1 = request.session.get('look1', '')
    context_dict['look1'] = look1
    look2 = request.session.get('look2', '')
    context_dict['look2'] = look2
    meterid = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(MeterId=meterid).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row2 = GS_MeterInfo_XZY.objects.filter(MeterId=meterid).values(
            'MeterId', 'Com_no_xzy', 'Sw_rlse_xzy', 'MeterNum', 'Temperature_xzy', 'Disturb_Total_Vol',
            'Pressure', 'Correction_E', 'Stan_Total_Vol', 'Stan_Ins_Ele_xzy', 'Work_Total_Vol', 'Work_Ins_Ele_xzy',
            'DropMeter1_xzy', 'DropMeter2_xzy', 'ReverseInstall1_xzy', 'ReverseInstall2_xzy', 'MeasureBreakdown1_xzy',
            'MeasureBreakdown2_xzy', 'TSensorBreakdown1_xzy', 'TSensorBreakdown2_xzy', 'PSensorBreakdown1_xzy',
            'PSensorBreakdown2_xzy',
            'TrafficAbnormality1_xzy', 'TrafficAbnormality2_xzy', 'ComVol1_xzy', 'ComVol2_xzy', 'BaseVol1_xzy',
            'BaseVol2_xzy',
            'CollectFault1_xzy', 'CollectFault1_xzy',
            'GasLeakClose1_xzy', 'GasLeakClose2_xzy', 'GasStolenClose1_xzy', 'GasStolenClose2_xzy',
             'ResetClose1_xzy', 'ResetClose2_xzy', 'LowVolClose1_xzy', 'LowVolClose2_xzy',
            'CollectClose1_xzy', 'CollectClose2_xzy', 'CommandClose1_xzy',
            'CommandClose2_xzy', 'ManulOpen1_xzy', 'ManulOpen2_xzy',
            'FTPUserName_xzy', 'FTPPassword_xzy', 'FTPAddress_xzy', 'FTPCatalog_xzy', 'FileName_xzy',
        ).first()
        form0 = MeterTypeForm(initial=row0)
        form2 = Meter_XZYForm(initial=row2)
        context_dict['meterid'] = meterid
        context_dict['metertype'] = metertype
        context_dict['form0'] = form0
        context_dict['form2'] = form2
        context_dict['msg0'] = form0.errors
        context_dict['msg2'] = form2.errors
        return render(request, 'check_xzy.html', context_dict)

def check_csb(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    look1 = request.session.get('look1', '')
    context_dict['look1'] = look1
    look2 = request.session.get('look2', '')
    context_dict['look2'] = look2
    meterid = request.GET.get('p1')
    metertype = request.GET.get('p2')
    if request.method == 'GET':
        row0 = GS_MeterTypeInfo.objects.filter(MeterId=meterid).values(
            'MeterId', 'MeterType', 'ManufactureName_id', 'TimeOfProduce',
        ).first()
        row2 = GS_MeterInfo_CSB.objects.filter(MeterId=meterid).values(
             'MeterId', 'Com_no_csb', 'Sw_rlse_csb', 'Vol1', 'Stan_Ins_Ele_csb', 'Vol2',
            'Work_Ins_Ele_csb', 'MeterStateWord', 'Temperature_csb', 'MeterInStateWord', 'PValue',
            'Stan_Total_Ele', 'Peak_Ele', 'Work_Total_Ele', 'DropMeter1_csb', 'DropMeter2_csb', 'ReverseInstall1_csb',
            'ReverseInstall2_csb', 'MeasureBreakdown1_csb', 'MeasureBreakdown2_csb', 'TSensorBreakdown1_csb',
            'TSensorBreakdown2_csb',
            'PSensorBreakdown1_csb', 'PSensorBreakdown2_csb', 'TrafficAbnormality1_csb', 'TrafficAbnormality2_csb',
            'ComVol1_csb', 'ComVol2_csb', 'BaseVol1_csb', 'BaseVol2_csb', 'CollectFault1_csb', 'CollectFault1_csb',
            'GasLeakClose1_csb', 'GasLeakClose2_csb',
            'GasStolenClose1_csb', 'GasStolenClose2_csb',
            'ResetClose1_csb', 'ResetClose2_csb', 'LowVolClose1_csb', 'LowVolClose2_csb', 'CollectClose1_csb',
            'CollectClose2_csb', 'CommandClose1_csb',
            'CommandClose2_csb', 'ManulOpen1_csb', 'ManulOpen2_csb',
            'AF_ULimit1', 'AF_DLimit1', 'AF_LLimit1', 'AF_ULimit2', 'AF_DLimit2',
            'AF_LLimit2', 'AF_ULimit3', 'AF_DLimit3', 'AF_LLimit3',
            'FTPUserName_csb', 'FTPPassword_csb', 'FTPAddress_csb', 'FTPCatalog_csb', 'FileName_csb',
        ).first()
        form0 = MeterTypeForm(initial=row0)
        form2 = Meter_CSBForm(initial=row2)
        context_dict['meterid'] = meterid
        context_dict['metertype'] = metertype
        context_dict['form0'] = form0
        context_dict['form2'] = form2
        context_dict['msg0'] = form0.errors
        context_dict['msg2'] = form2.errors
        return render(request, 'check_csb.html', context_dict)

#测试人员开始进行审核
def check(request):
    context_dict = {}
    reinfo = getminfo(request)
    if request.method == 'POST':
        meterid = request.POST['MeterId']
        result = request.POST['result']
        try:
            CheckTime = datetime.datetime.now()
            meter = GS_MeterTypeInfo.objects.get(MeterId=meterid)
            meter.check_user = reinfo[0]
            meter.CheckTime = CheckTime
            meter.IsDataChecked = 1  # 已审核
            if result == "1":
                meter.DataCheckedResult = 1  # 通过
            else:
                meter.DataCheckedResult = 0  # 不通过
            meter.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")

#重审
def back(request):
    if request.method == "POST":
        MeterId = request.POST['MeterId']
        try:
            try:
                meter = Meter_Test.objects.get(MeterId=MeterId)
            except:
                meter = None
            if meter:
                return HttpResponse("3")
            else:
                GS_MeterTypeInfo.objects.filter(MeterId=MeterId).update(
                    IsDataChecked=0,
                    DataCheckedResult=0,
                    IsAllocated=0,
                    IsTest=0,
                    CommandTest=None,
                    ICTest=None,
                    ChuTest=None,
                    ZhoTest=None,
                    MianTest=None,
                )
                return HttpResponse("1")
        except:
            return HttpResponse("2")

#测试人员看到的所有审核结果
def checkresult(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    search_dict = dict()
    if request.method == 'GET':
        q_form = MeterQueryForm4()
        context_dict['q_form'] = q_form
        # 分页
        all_count = GS_MeterTypeInfo.objects.filter(IsSubmit=1, IsDataChecked=1).count()
        current_page = request.GET.get('page')
        page_info = PageInfo(current_page, all_count, 10, '/checkresult/', 11)
        meter_list = GS_MeterTypeInfo.objects.filter(IsSubmit=1, IsDataChecked=1)[page_info.start():page_info.end()]
        context_dict['meter_list'] = meter_list
        context_dict['page_info'] = page_info  # 不要忘了传到前端
        return render(request, 'checkresult.html',context_dict)
    else:
        q_form = MeterQueryForm4(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            checktime = q_form.cleaned_data['CheckTime']
            manu = q_form.cleaned_data['ManufactureName_id']
            meterstate = q_form.cleaned_data['DataCheckedResult']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if meterstate:
                search_dict['DataCheckedResult'] = meterstate
            if manu:
                search_dict['ManufactureName_id'] = manu
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            if checktime:
                search_dict['CheckTime__year'] = checktime.year
                search_dict['CheckTime__month'] = checktime.month
                search_dict['CheckTime__day'] = checktime.day
            info = GS_MeterTypeInfo.objects.filter(IsSubmit=1, IsDataChecked=1,**search_dict)
            context_dict['meter_list'] = info
            return render(request, 'checkresult.html', context_dict)
        else:
            q_form = MeterQueryForm4()
            return  HttpResponse("not found 404")

#分配测试任务
#显示待分配的燃气表
def allocation(request):
    context_dict = {}
    user = request.session.get('user', '')
    context_dict['user'] = user
    search_dict = dict()
    if request.method == 'GET':
        q_form = MeterQueryForm5()
        context_dict['q_form'] = q_form
        # 分页
        all_count = GS_MeterTypeInfo.objects.filter(DataCheckedResult=1,IsAllocated=0).count()
        current_page = request.GET.get('page')
        page_info = PageInfo(current_page, all_count, 10, '/allocation/', 11)
        meter_list = GS_MeterTypeInfo.objects.filter(DataCheckedResult=1,IsAllocated=0)[page_info.start():page_info.end()]
        context_dict['meter_list'] = meter_list
        context_dict['page_info'] = page_info  # 不要忘了传到前端
        return render(request, 'allocation.html',context_dict)
    else:
        q_form = MeterQueryForm5(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            checktime = q_form.cleaned_data['CheckTime']
            manu = q_form.cleaned_data['ManufactureName_id']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if manu:
                search_dict['ManufactureName_id'] = manu
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            if checktime:
                search_dict['CheckTime__year'] = checktime.year
                search_dict['CheckTime__month'] = checktime.month
                search_dict['CheckTime__day'] = checktime.day
            info = GS_MeterTypeInfo.objects.filter(DataCheckedResult=1,IsAllocated=0, **search_dict)
            context_dict['meter_list'] = info
            return render(request, 'allocation.html', context_dict)
        else:
            q_form = MeterQueryForm5()
            return HttpResponse("not found 404")

#提交分配结果
def sub_allocation(request):
    context_dict = {}
    reinfo = getminfo(request)
    if request.method == 'POST':
        MeterId = request.POST['MeterId']
        MeterType = request.POST['MeterType']
        checkID = request.POST.getlist('checkID')
        try:
            meter = GS_MeterTypeInfo.objects.get(MeterId=MeterId)
            meter.allo_user = reinfo[0]
            meter.IsAllocated = 1
            MeterState = '初始'
            if '1' in checkID:
                meter.MeterPrivilege = '1'
            else:
                meter.MeterPrivilege = '1'
            if 'IC卡检测' in checkID:
                meter.ICTest = '待测'
            else:
                meter.ICTest = '不测'
            if '初检' in checkID:
                meter.ChuTest = '待测'
            else:
                meter.ChuTest = '不测'
            if '命令检测' in checkID:
                meter.CommandTest = '待测'
            else:
                meter.CommandTest = '不测'
            if '终检' in checkID:
                meter.ZhoTest = '待测'
            else:
                meter.ZhoTest = '不测'
            if '免检' in checkID:
                meter.MianTest = '合格'
                MeterState = '合格'
            else:
                meter.MianTest = '否'
            meter.save()
            try:
                Meter_Test.objects.create(
                    MeterId = MeterId,
                    MeterType = MeterType,
                    MeterComState = meter.CommandTest,
                    MeterIcState = meter.ICTest,
                    MeterChuState = meter.ChuTest,
                    MeterZhongState = meter.ZhoTest,
                    MeterState = MeterState,
                    MeterPrivilege=meter.MeterPrivilege,
                    ManufactureName_id=meter.ManufactureName_id,
                    CheckTime=meter.CheckTime,
                    Subtime=meter.Subtime,
                )
                return HttpResponse("1")
            except IntegrityError:
                return HttpResponse("2")
        except:
            return HttpResponse("2")

#显示分配结果
def allo_result(request):
    context_dict = {}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    search_dict = dict()
    if request.method == 'GET':
        q_form = MeterQueryForm5()
        context_dict['q_form'] = q_form
        all_count = GS_MeterTypeInfo.objects.filter(DataCheckedResult=1,IsAllocated=1).count()
        current_page = request.GET.get('page')
        page_info = PageInfo(current_page, all_count, 10, '/allo_result/', 11)
        meter_list = GS_MeterTypeInfo.objects.filter(DataCheckedResult=1,IsAllocated=1)[page_info.start():page_info.end()]
        for m in meter_list:
            if m.MeterPrivilege == '1':
                m.MeterPrivilege = '是'
            else:
                m.MeterPrivilege = '否'
        context_dict['meter_list'] = meter_list
        context_dict['page_info'] = page_info  # 不要忘了传到前端
        return render(request, 'allo_result.html', context_dict)
    else:
        q_form = MeterQueryForm5(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            checktime = q_form.cleaned_data['CheckTime']
            manu = q_form.cleaned_data['ManufactureName_id']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if manu:
                search_dict['ManufactureName_id'] = manu
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            if checktime:
                search_dict['CheckTime__year'] = checktime.year
                search_dict['CheckTime__month'] = checktime.month
                search_dict['CheckTime__day'] = checktime.day
            info = GS_MeterTypeInfo.objects.filter(DataCheckedResult=1, IsAllocated=1, **search_dict)
            context_dict['meter_list'] = info
            return render(request, 'allo_result.html', context_dict)
        else:
            q_form = MeterQueryForm5()
            return HttpResponse("not found 404")

#删除分配结果（不用）
def del_allo(request):
    if request.method=="POST":
        MeterToDel = request.POST['MeterId']
        try:
            try:
                meter = Meter_Test.objects.get(MeterId=MeterToDel)
            except:
                meter = None
            if meter:   #查到了就不能改了
                return HttpResponse("3")  #表已经开始测试了，无法操作
            else:
                try:
                    meter_finish = Meter_Fail.objects.get(MeterId=MeterToDel)
                except:
                    try:
                        meter_finish = Meter_Success.objects.get(MeterId=MeterToDel)
                    except:
                        meter_finish = None
                if meter_finish:
                    return HttpResponse("4")  # 测试完成但没有移走
                else:
                    GS_MeterTypeInfo.objects.filter(MeterId=MeterToDel).update(
                        IsAllocated=0
                    )
                    return HttpResponse("1")
        except:
            return HttpResponse("2")

# 获得生产厂商
def getmanu(m):
    meters_meterid = m.MeterId
    try:
        item = GS_MeterTypeInfo.objects.get(MeterId=meters_meterid)
        m.Manu = item.ManufactureName.ManufactureName
    except:
        m.Manu = None
    return m

#获得该表测试时的服务器
def getplat(m):
    meters_meterid = m.MeterId
    try:
        item = MeterPlat.objects.get(MeterId=meters_meterid)
        try:
            ii = Meter_Test.objects.get(MeterId=meters_meterid)
            if item.Meterip_Com != '-1':
                m.Meterip_Com = item.Meterip_Com
            elif item.Meterip_Com == '-1' and ii.MeterComState == '待测':
                m.Meterip_Com = "未分配"
            else:
                m.Meterip_Com = "无"
            if item.Meterip_IC != '-1':
                m.Meterip_IC = item.Meterip_IC
            elif item.Meterip_IC == '-1' and ii.MeterIcState == '待测':
                m.Meterip_IC = "未分配"
            else:
                m.Meterip_IC = "无"
            if item.Meterip_Chu != '-1':
                m.Meterip_Chu = item.Meterip_Chu
            elif item.Meterip_Chu == '-1' and ii.MeterChuState == '待测':
                m.Meterip_Chu = "未分配"
            else:
                m.Meterip_Chu = "无"
            if item.Meterip_Zhong != '-1':
                m.Meterip_Zhong = item.Meterip_Zhong
            elif item.Meterip_Zhong == '-1' and ii.MeterZhongState == '待测':
                m.Meterip_Zhong = "未分配"
            else:
                m.Meterip_Zhong = "无"
        except:
               if item.Meterip_Com != '-1':
                   m.Meterip_Com = item.Meterip_Com
               else:
                   m.Meterip_Com = "无"
               if item.Meterip_IC != '-1':
                   m.Meterip_IC = item.Meterip_IC
               else:
                   m.Meterip_IC = "无"
               if item.Meterip_Chu != '-1':
                   m.Meterip_Chu = item.Meterip_Chu
               else:
                   m.Meterip_Chu = "无"
               if item.Meterip_Zhong != '-1':
                   m.Meterip_Zhong = item.Meterip_Zhong
               else:
                   m.Meterip_Zhong = "无"
    except:
        item = None
        try:
            ii = Meter_Test.objects.get(MeterId=meters_meterid)
            if ii.MeterComState == '待测':
                m.Meterip_Com = "未分配"
            else:
                m.Meterip_Com = "无"
            if ii.MeterIcState == '待测':
                m.Meterip_IC = "未分配"
            else:
                m.Meterip_IC = "无"
            if ii.MeterChuState == '待测':
                m.Meterip_Chu = "未分配"
            else:
                m.Meterip_Chu = "无"
            if ii.MeterZhongState == '待测':
                m.Meterip_Zhong = "未分配"
            else:
                m.Meterip_Zhong = "无"
        except:
            ii =None
    return m

#修改正在测试的项目结果状态
def getstate(m):
    try:
        mstate = m.Meteriport.split('@')[3]  # 获得正在测试的项目
    except:
        mstate = None
    if mstate != None and m.MeterTest == '正测':
        m.MeterState = "进行中"
        if 'Com' in mstate and m.MeterTest == '正测':
            m.MeterComState = "进行中"
        if 'Ic' in mstate and m.MeterTest == '正测':
            m.MeterIcState = "进行中"
        if 'Chu' in mstate and m.MeterTest == '正测':
            m.MeterChuState = "进行中"
        if 'Zhong' in mstate and m.MeterTest == '正测':
            m.MeterZhongState = "进行中"
    if m.MeterTest == '准备':
        m.MeterState = "准备"
    if m.MeterTest == '就绪':
        m.MeterState = "就绪"
    return m

#解析单项数据结果
def getev_result(re):
    if re == 'AA':
        ev_result = "合格"
    elif re == '55':
        ev_result = "不合格"
    else:
        ev_result = "不测"
    return ev_result

def every_result(m):
    mev_result = m.MeterEvery
    chu_result = mev_result[0:10]    #四项单项
    m.changgui = getev_result(chu_result[0:2])
    m.miyao = getev_result(chu_result[2:4])
    m.canshu = getev_result(chu_result[4:6])
    m.FTP = getev_result(chu_result[6:8])
    ic_result = mev_result[10:14]    #无单项
    com_result = mev_result[14:20]   #两项单项
    m.chang = getev_result(com_result[14:16])
    m.wrong = getev_result(com_result[16:18])
    zho_result = mev_result[20:32]   #五项单项
    m.moni = getev_result(zho_result[20:22])
    m.hefa = getev_result(zho_result[22:24])
    m.shangchuan = getev_result(zho_result[24:26])
    m.caijitime = getev_result(zho_result[26:28])
    m.caijicircle = getev_result(zho_result[28:30])
    return m

def middle_result(request):
    context_dict = {}
    meters = []
    mmeters = []
    search_dict = dict()
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    context_dict['group'] = reinfo[1]
    if request.method == 'GET':
        q_form = MeterQueryForm5()
        context_dict['q_form'] = q_form
        # 自动入库
        try:
            meter_move = Meter_Result.objects.filter(Q(MeterState="完成") | Q(MeterState="不合格") | Q(MeterState="失败"))
        except:
            meter_move = None
        if meter_move:
            for m in meter_move:
                Meter_Result_Record.objects.create(
                    MeterId=m.MeterId,
                    MeterType=m.MeterType,
                    MeterComState=m.MeterComState,
                    MeterIcState=m.MeterIcState,
                    MeterChuState=m.MeterChuState,
                    MeterZhongState=m.MeterZhongState,
                    MeterState=m.MeterState,
                    MeterTest=m.MeterTest,
                    MeterRand_num=m.MeterRand_num,
                    Meteriport=m.Meteriport,
                    MeterTime=m.MeterTime,
                    MeterCancel=m.MeterCancel,
                    MeterEvery=m.MeterEvery,
                    MeterPrivilege=m.MeterPrivilege,
                    ManufactureName_id=m.ManufactureName_id,
                    Subtime=m.Subtime,
                    CheckTime=m.CheckTime,
                )
                m.delete()
                GS_MeterTypeInfo.objects.filter(MeterId=m.MeterId).update(IsTest=1)
        if reinfo[1] != '生产厂商':
            try:
                meterlist = Meter_Test.objects.all()
            except:
                meterlist  =None
            if meterlist:
                for meter in meterlist:
                    every_result(meter)
                    getmanu(meter)
                    getstate(meter)
                    getplat(meter)
                    meters.append(meter)
            context_dict['meter_list'] = meters
            return render(request, 'middle_result.html', context_dict)
        else:
            try:
                meterlist = Meter_Test.objects.filter(ManufactureName_id=reinfo[2])
            except:
                meterlist = None
            if meterlist:
                for meter in meterlist:
                    every_result(meter)
                    getmanu(meter)
                    getstate(meter)
                    getplat(meter)
                    meters.append(meter)
            context_dict['meter_list'] = meters
            return render(request, 'middle_result.html', context_dict)
    else:
        q_form = MeterQueryForm5(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            checktime = q_form.cleaned_data['CheckTime']
            manu = q_form.cleaned_data['ManufactureName_id']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if manu:
                search_dict['ManufactureName_id'] = manu
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            if checktime:
                search_dict['CheckTime__year'] = checktime.year
                search_dict['CheckTime__month'] = checktime.month
                search_dict['CheckTime__day'] = checktime.day
            if reinfo[1] != '生产厂商':
                try:
                    meters = Meter_Test.objects.filter(**search_dict)
                except:
                    meters = None
                if meters:
                    for meter in meters:
                        every_result(meter)
                        getmanu(meter)
                        getstate(meter)
                        getplat(meter)
                        mmeters.append(meter)
                context_dict['meter_list'] = mmeters
                return render(request,'middle_result.html', context_dict)
            else:
                try:
                    meters = Meter_Test.objects.filter(ManufactureName_id=reinfo[2],**search_dict)
                except:
                    meters = None
                if meters:
                    for meter in meters:
                        every_result(meter)
                        getmanu(meter)
                        getstate(meter)
                        getplat(meter)
                        mmeters.append(meter)
                context_dict['meter_list'] = mmeters
                return render(request,'middle_result.html', context_dict)

#再次检测(不用）
def again_test(request):
    if request.method == "POST":
        MeterId = request.POST['MeterId']
        print(MeterId)
        try:
            meter = Meter_Result.objects.get(MeterId=MeterId)
            print("成功找到")
            Meter_Result_Record.objects.create(
                MeterId = meter.MeterId,
                MeterType = meter.MeterType,
                MeterComState = meter.MeterComState,
                MeterIcState = meter.MeterIcState,
                MeterChuState = meter.MeterChuState,
                MeterZhongState = meter.MeterZhongState,
                MeterState = meter.MeterState,
                MeterTest = meter.MeterTest,
                MeterRand_num = meter.MeterRand_num,
                Meteriport = meter.Meteriport,
                MeterTime = meter.MeterTime,
                MeterCancel = meter.MeterCancel,
            )
            print("成功创建")
            meter.delete()
            print("成功删除")
            GS_MeterTypeInfo.objects.filter(MeterId=MeterId).update(
                IsAllocated = 0,
                CommandTest =None,
                ICTest = None,
                ChuTest = None,
                ZhoTest = None,
                MianTest = None,
            )
            print("成功修改")
            return HttpResponse("1")
        except:
            return HttpResponse("2")
    else:
        return HttpResponse("2")

#入库操作（不用）
def storage(request):
    if request.method == "POST":
        MeterId = request.POST['MeterId']
        try:
            meter = Meter_Result.objects.get(MeterId=MeterId)
            Meter_Result_Record.objects.create(
                MeterId = meter.MeterId,
                MeterType = meter.MeterType,
                MeterComState = meter.MeterComState,
                MeterIcState = meter.MeterIcState,
                MeterChuState = meter.MeterChuState,
                MeterZhongState = meter.MeterZhongState,
                MeterState = meter.MeterState,
                MeterTest = meter.MeterTest,
                MeterRand_num = meter.MeterRand_num,
                Meteriport = meter.Meteriport,
                MeterTime = meter.MeterTime,
                MeterCancel = meter.MeterCancel,
            )
            meter.delete()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
    else:
        return HttpResponse("2")

def del_test(request):
    if request.method == "POST":
        MeterId = request.POST['MeterId']
        try:
            GS_MeterTypeInfo.objects.filter(MeterId=MeterId).update(
                IsAllocated=0,
                CommandTest=None,
                ICTest=None,
                ChuTest=None,
                ZhoTest=None,
                MianTest=None,
            )
            Meter_Result.objects.get(MeterId=MeterId).delete()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
    else:
        return HttpResponse("2")

#测试结果
def result(request):
    context_dict = {}
    meters = []
    search_dict = dict()
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    context_dict['group'] = reinfo[1]
    if request.method == 'GET':
        q_form = MeterQueryForm5()
        context_dict['q_form'] = q_form
        return render(request, 'result.html', context_dict)
    else:
        q_form = MeterQueryForm5(request.POST)
        context_dict['q_form'] = q_form
        if q_form.is_valid():
            meterid = q_form.cleaned_data['MeterId']
            metertype = q_form.cleaned_data['MeterType']
            subtime = q_form.cleaned_data['Subtime']
            checktime = q_form.cleaned_data['CheckTime']
            manu = q_form.cleaned_data['ManufactureName_id']
            if meterid:
                search_dict['MeterId'] = meterid
            if metertype:
                search_dict['MeterType'] = metertype
            if manu:
                search_dict['ManufactureName_id'] = manu
            if subtime:
                search_dict['Subtime__year'] = subtime.year
                search_dict['Subtime__month'] = subtime.month
                search_dict['Subtime__day'] = subtime.day
            if checktime:
                search_dict['CheckTime__year'] = checktime.year
                search_dict['CheckTime__month'] = checktime.month
                search_dict['CheckTime__day'] = checktime.day
            if reinfo[1] != '生产厂商':
                meterlist = Meter_Result_Record.objects.filter(**search_dict)
                if meterlist:
                    for m in meterlist:
                        every_result(m)
                        getmanu(m)
                        getplat(m)
                        getstate(m)
                        meters.append(m)
                context_dict['meter_list'] = meters
                return render(request, 'result.html', context_dict)
            else:
                try:
                    meterlist = Meter_Result_Record.objects.filter(ManufactureName_id=reinfo[2],**search_dict)
                except:
                    meterlist = None
                if meterlist:
                    for meter in meterlist:
                        every_result(meter)
                        getmanu(meter)
                        getplat(meter)
                        getstate(meter)
                        meters.append(meter)
                context_dict['meter_list'] = meters
                return render(request, 'result.html', context_dict)

#用户管理
#显示已登录用户信息
def user(request):
    context_dict={}
    reinfo = getminfo(request)
    context_dict['user'] = reinfo[0]  # 用户名传给前端
    context_dict['user_id'] = reinfo[3]  #用户的ID
    return render(request,'user.html',context_dict)

