from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def add(request):
    dict = request.GET
    gid = int(dict.get('gid'))
    count = int(dict.get('count'))
    uid = request.session.get('uid')

    # 查询当前用户是否购买过此商品，如果购买直接加数量
    carts = CartInfo.objects.filter(cuser__id=uid, cgood__id=gid)

    if len(carts) == 0:
        cart = CartInfo()
        cart.cuser_id = request.session.get('uid')
        cart.cgood_id = gid
        cart.ccoumt = count
        cart.save()
    else:
        cart = carts[0]
        cart.ccoumt+=count
        cart.save()
    return JsonResponse({'ok': 1})
