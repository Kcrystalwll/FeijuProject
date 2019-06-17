from django.conf import settings
from django.shortcuts import HttpResponse
import re

# 自定义类，继承MiddlewareMixin
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class PermissionMiddle(MiddlewareMixin):
    def process_request(self,request):
        #对权限进行校验
        # 当前访问的URL
        current_url = request.path_info

        #白名单的判断(无需校验的URL)
        for item in settings.WHITE_URL_LIST:
            if re.match(item,current_url):
                return

        #当前用户所有权限信息
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        #权限的校验
        #注意：permission_list是列表的集合，current_url是单个列表
        if permission_list:
            for item in permission_list:
                url = item['url']
                if re.match("^{}$".format(url),current_url):
                    # id = item['id']
                    # pid = item['pid']
                    # if pid:
                    #     #表示当前权限是子权限
                    #     request.current_menu_id=pid
                    # else:
                    #     #表示当前权限是父权限，是二级菜单
                    #     request.current_menu_id = id
                    return
            else:
                return HttpResponse('无访问权限')

