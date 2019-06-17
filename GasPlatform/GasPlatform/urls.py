"""GasPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mygas import views as mygas_views
from rbac import views as rbac_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/', mygas_views.login),
    url(r'^logout/', mygas_views.logout),

    url(r'^index/', mygas_views.index),
    url(r'^print/', mygas_views.prin),

    url(r'^export_excel/', mygas_views.export_excel),
    url(r'^data/', mygas_views.data),
    url(r'^submit/', mygas_views.submit),
    url(r'^dataresult/', mygas_views.dataresult),  #显示审核的情况，厂商看的
    url(r'^datainput/', mygas_views.datainput),
    url(r'^datainput_ic_msb/', mygas_views.datainput_ic_msb),
    url(r'^datainput_ic_xzy/', mygas_views.datainput_ic_xzy),
    url(r'^datainput_ic_csb/', mygas_views.datainput_ic_csb),
    url(r'^datainput_msb/', mygas_views.datainput_msb),
    url(r'^datainput_csb/', mygas_views.datainput_csb),
    url(r'^datainput_xzy/', mygas_views.datainput_xzy),

    url(r'^del_data/', mygas_views.del_data),
    url(r'^edit_data/', mygas_views.edit_data),
    url(r'^edit_ic_msb/', mygas_views.edit_ic_msb),
    url(r'^edit_ic_xzy/', mygas_views.edit_ic_xzy),
    url(r'^edit_ic_csb/', mygas_views.edit_ic_csb),
    url(r'^edit_msb/', mygas_views.edit_msb),
    url(r'^edit_xzy/', mygas_views.edit_xzy),
    url(r'^edit_csb/', mygas_views.edit_csb),

    url(r'^datacheck/', mygas_views.datacheck),    #显示待审核的燃气表
    url(r'^check_data/', mygas_views.check_data),  #表类型跳转

    url(r'^check_ic_msb/', mygas_views.check_ic_msb),
    url(r'^check_ic_xzy/', mygas_views.check_ic_xzy),
    url(r'^check_ic_csb/', mygas_views.check_ic_csb),
    url(r'^check_msb/', mygas_views.check_msb),
    url(r'^check_xzy/', mygas_views.check_xzy),
    url(r'^check_csb/', mygas_views.check_csb),

    url(r'^check/', mygas_views.check), #数据审核操作，测试人员操作的
    url(r'^checkresult/', mygas_views.checkresult), #数据审核结果，测试人员看的

    url(r'^back/', mygas_views.back),

    url(r'^allocation/', mygas_views.allocation),
    url(r'^sub_allocation/', mygas_views.sub_allocation),
    url(r'^allo_result/', mygas_views.allo_result),
    url(r'^del_allo/', mygas_views.del_allo),

    url(r'^middle_result/', mygas_views.middle_result),
    url(r'^again_test/', mygas_views.again_test),
    url(r'^storage/', mygas_views.storage),
    url(r'^del_test/', mygas_views.del_test),
    url(r'^result/', mygas_views.result),  #最终测试结果

    url(r'^user/', mygas_views.user),
    # url(r'^users/', mygas_views.users),
    #
    # url(r'^user_edit/', mygas_views.user_edit),
    # url(r'^userpermit_edit/', mygas_views.userpermit_edit),
    # url(r'^user_delete/', mygas_views.user_delete),
    # url(r'^user_add/', mygas_views.user_add),

    #权限rbac
    url(r'^group/', rbac_views.group),
    url(r'^group_add/', rbac_views.group_add),
    url(r'^group_del/', rbac_views.group_del),
    url(r'^group_edit/', rbac_views.group_edit),

    url(r'^manulist/', rbac_views.manulist),
    url(r'^manulist_add/', rbac_views.manulist_add),
    url(r'^manulist_del/', rbac_views.manulist_del),
    url(r'^manulist_edit/', rbac_views.manulist_edit),

    url(r'^permissionlist_del/', rbac_views.permissionlist_del),

    url(r'^loginuser_add/', rbac_views.loginuser_add),
    url(r'^loginuser_edit/', rbac_views.loginuser_edit),
    url(r'^loginuser_del/', rbac_views.loginuser_del),
    url(r'^pwd_reset/', rbac_views.pwd_reset),
]
