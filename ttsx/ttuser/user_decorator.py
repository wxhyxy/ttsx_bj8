# coding = utf-8
from django.shortcuts import redirect

#装饰器验证用户有没有登陆
def user_login(fun):
    def fun2(request, *args, **kwargs):
        # 跟据session 里有没有uid 值做判断
        if request.session.has_key('uid'):
            return fun(request, *args, **kwargs)
        else:
            return redirect('/ttuser/login/')
    return fun2