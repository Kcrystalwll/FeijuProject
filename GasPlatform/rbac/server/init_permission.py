from django.conf import settings
def init_permission(request,user):
    # 将权限信息写入session
    permission_dict = user.group.all().values(
        'permission__url',
        'permission__icon',
        'permission__menu_name',
        'permission__menu_id',
        #三级菜单（不用显示的菜单）
        # 'permission__id'
        # 'permission__parent_id'
        #一级
        'permission__menu__menu_name',
        'permission__menu__icon',
        'permission__menu__weight',
    ).distinct()
    # for i in permission_dict:
    #     print(i)

    permission_list = []
    menu_dict = {}
    for item in permission_dict:
        # URL
        permission_list.append(
            {'url': item['permission__url'],
             # 'id': item['permission_id'],
             # 'pid': item['permission__parent_id'],
             }
        )

        menu_id = item.get('permission__menu_id')

        if not menu_id:
            continue

        #第一次进入
        if menu_id not in menu_dict:
            menu_dict[menu_id] = {
                'menu_name':item['permission__menu__menu_name'],
                'icon':item['permission__menu__icon'],
                'weight':item['permission__menu__weight'],
                'children':[
                    {
                        'menu_name':item['permission__menu_name'],
                        'url':item['permission__url'],
                        'icon':item['permission__icon'],
                        # 'id':item['permission__id'],
                        # 'pid':item['permission__parent_id'],
                    }
                ],
            }
        #第二个孩子
        else:
            menu_dict[menu_id]['children'].append(
                {
                    'menu_name': item['permission__menu_name'],
                    'url': item['permission__url'],
                    'icon': item['permission__icon'],
                    # 'id': item['permission__id'],
                    # 'pid': item['permission__parent_id'],
                }
            )
    # print(menu_dict)
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_dict

    #     if item.get('permission__is_menu'):
    #         # 菜单
    #         menu_list.append(
    #             {'url': item['permission__url'],
    #              'icon': item['permission__icon'],
    #              'menu_name': item['permission__menu_name'],
    #              })
    # print(permission_list)
    # print(menu_list)
    # # session把元组转换成列表
    # request.session[settings.PERMISSION_SESSION_KEY] = list(permission_list)
    # request.session[settings.MENU_SESSION_KEY] = list(menu_list)