from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    typeinfo = TypeInfo.objects.all()
    list = []
    for type in typeinfo:
        list.append({
            'type':type,
            'list_new':type.goodsinfo_set.order_by('-id')[0:4],
            'list_click':type.goodsinfo_set.order_by('gclick')[0:3]
        })

    context = {'title':'首页', 'list':list, 'cart' : '1'}
    return render(request, 'tt_good/index.html', context)

def list_goods(request, type_id):
    typeinfo = TypeInfo.objects.get(pk=type_id)
    list = typeinfo.goodsinfo_set.order_by('id')
    context = {'title':'列表', 'cart':'1', 'type':typeinfo, 'list':list}
    return render(request, 'tt_good/list.html',context)