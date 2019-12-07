from django.shortcuts import render, redirect, HttpResponse
from functools import wraps
from data_system import models
from utils import my_page
from django.contrib.auth import authenticate, login
from users import models as users
import time

# Create your views here.

def main(request):
    # 获取session中的用户名
    username = request.session.get('username', None)
    # 页码数即当前为第几页
    page_num = request.GET.get('page')
    # # 每页显示条目数
    per_page = per_num(request)
    print(per_page)
    # 从数据库中获取化学物质条目
    chemical_list = models.Chemicals.objects.all()
    # 数据库中获得化学物质条目数量
    total_count = chemical_list.count()
    # 调用写好的分页的类
    page_obj = my_page.Page(page_num, total_count, url_prefix='/home/', per_page=per_page, max_page=9)
    # 当前页面显示的化学物质条目编号始终
    chemical_list = models.Chemicals.objects.all()[page_obj.start:page_obj.end]
    # 根据用户名获取数据库对象
    sign_obj = users.UserInfo.objects.get(username=username)

    # 获取分页的HTML代码
    page_html = page_obj.page_html()
    # 传入前端的参数字典
    data_dict = {
        'chemicals': chemical_list,
        'page_html': page_html,
        'obj': page_obj,
        'total_count': total_count,
        'username': username,
        'date_joined': sign_obj.date_joined,
        'name': sign_obj.name,
        'sign_img': sign_obj.image,
    }
    return render(request, 'starter.html', data_dict)


def per_num(request):
    if request.GET.get('per_num'):
        return request.GET.get('per_num')
    else:
        per = 10
        return per