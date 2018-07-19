from django.shortcuts import render, redirect
from django.http import JsonResponse
from hashlib import sha1
from .models import *
import datetime
from .user_decorator import *
from ttgood.models import *


# Create your views here.
def regisger(request):
    return render(request, 'ttuser/register.html', {'title': '注册', 'top':'0'})


def register_handle(request):
    dic = request.POST
    uname = dic.get('user_name')
    upwd = dic.get('pwd')
    cpwd = dic.get('cpwd')
    uemail = dic.get('email')
    if upwd != cpwd:
        return redirect('/user/register/')
    s1 = sha1()
    s1.update(upwd.encode())
    upwd1 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd1
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')


def login(request):
    uname = request.COOKIES.get('uname')
    return render(request, 'ttuser/login.html', {'title': '登陆', 'top':'0', 'uname':uname})


def register_valid(request):
    dict = request.GET
    uname = dict.get('uname')
    result = UserInfo.objects.filter(uname=uname).count()
    content = {'valid': result}
    return JsonResponse(content)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('userpwd')
    # 代表记住名字
    uname_jz = post.get('name_jz', '0')

    s1 = sha1()
    s1.update(upwd.encode())
    sha_pwd = s1.hexdigest()

    context = {'title': '登陆', 'uname': uname, 'upwd': upwd, 'top':'0'}

    user = UserInfo.objects.filter(uname=str(uname))  # 返回一个列表

    if len(user) == 0:
        context['name_error'] = '1'
        return render(request, 'ttuser/login.html', context)
    else:
        # 判断密码是否正确
        if user[0].upwd == sha_pwd:
            request.session['uid'] = user[0].id
            request.session['uname'] = uname
            # 重定向 ， 哪里传过来的 返回到哪里
            path = request.session.get('url_path', '/')
            response = redirect(path)

            # 记住名字 判断 然后进行操作
            if uname_jz == '1':
                # 用户名存cookie
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            context['pwd_error'] = '1'
            return render(request, 'ttuser/login.html', context)

def login_out(request):
    request.session.flush()
    return redirect('/user/login/')

@user_login
def center(request):
    # 根据村的session 获得 user对象
    user = UserInfo.objects.get(pk=request.session.get('uid'))
    goods_ids = request.COOKIES.get('goods_ids').split(',')
    # good = GoodsInfo.objects.filter(id__in=goods_ids)
    # 最近浏览
    good_list = []
    for gid in goods_ids:
        if gid:
            good_list.append(GoodsInfo.objects.get(id=gid))
    context = {'title':'用户中心','user':user, 'good':good_list}
    return render(request, 'ttuser/user_center_info.html', context)

@user_login
def order(request):
    user = UserInfo.objects.get(pk=request.session.get('uid'))
    context={'title':'用户订单','user':user}
    return render(request, 'ttuser/user_center_order.html', context)

@user_login
def site(requset):
    user = UserInfo.objects.get(pk=requset.session.get('uid'))
    if requset.method == 'POST':
        post = requset.POST
        user.ushou = post.get('ushou')
        sheng = AreaInfo.objects.get(id=post.get('sheng'))
        shi = AreaInfo.objects.get(id=post.get('shi'))
        qu = AreaInfo.objects.get(id=post.get('qu'))
        user.uaddr = str(sheng.atitle) + str(shi.atitle) + str(qu.atitle) + str(post.get('input'))
        user.uphone = post.get('uphone')
        user.save()
    context = {'title':'收货地址','user':user}
    return render(requset, 'ttuser/user_center_site.html',context)

def area(request):
    # 省的父级为空，找出省的对象，构建Json形式的列表
    sheng = AreaInfo.objects.filter(aPentar__isnull=True)
    dic = []
    for item in sheng:
        dic.append([item.id, item.atitle])
    return JsonResponse({'data':dic})

def area1(request, pid):
    shi = AreaInfo.objects.filter(aPentar_id=pid)
    dic = []
    for item in shi:
        dic.append([item.id, item.atitle])
    return JsonResponse({'data':dic})