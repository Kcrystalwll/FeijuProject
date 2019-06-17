from django import template

register = template.Library()

from django.conf import settings
import re
from collections import OrderedDict

@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    # for item in menu_list:
    #     url = item['url']
    #     if re.match('^{}$'.format(url),request.path_info):
    #         item['class'] = 'active'
    order_dict = OrderedDict()

    #以key排序
    for key in sorted(menu_list,key=lambda x:menu_list[x]['weight'],reverse=True):
        order_dict[key] = menu_list[key]

        item = order_dict[key]

        # item['class'] = 'hide'

        for i in item['children']:
            if re.match('^{}$'.format(i['url']), request.path_info):
                i['class'] = 'active'
                # item['class'] = ''

    return {"menu_list":order_dict}

@register.simple_tag
def gen_role_url(request,rid):
    params = request.GET.copy()
    params._mutable = True
    params['rid'] = rid
    return params.urlencode()

