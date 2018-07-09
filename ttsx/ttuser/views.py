from django.shortcuts import render,redirect
from hashlib import sha1
from .models import *

# Create your views here.
def regisger(request):
    return render(request, 'ttuser/register.html')

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
    return render(request, 'ttuser/login.html')
