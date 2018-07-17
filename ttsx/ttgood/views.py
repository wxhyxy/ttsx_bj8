from django.shortcuts import render
from django.core.paginator import Paginator
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

def list_goods(request, type_id, pindex):
    typeinfo = TypeInfo.objects.get(pk=type_id)
    list = typeinfo.goodsinfo_set.order_by('id')
    page_list = Paginator(list, 10)
    if int(pindex)<1:
        pindex = 1
    elif int(pindex)>=page_list.num_pages:
        pindex = page_list.num_pages
    page = page_list.page(pindex)

    plist = page_list.page_range
    if page_list.num_pages < 5:
        if int(pindex) <= 2:
            plist = range(1, 6)
        elif int(pindex) >= page_list.num_pages:
            plist = range(page_list.num_pages-4, page_list.num_pages+1)
        else:
            plist = range(pindex-2, plist+3)

    context = {'title':'列表', 'cart':'1', 'type':typeinfo, 'list':page, 'plist':plist}
    return render(request, 'tt_good/list.html',context)