from django.shortcuts import render
from django.core.paginator import Paginator
from ttuser.models import *
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

def list_goods(request, type_id, pindex, order_by):
    typeinfo = TypeInfo.objects.get(pk=type_id)
    order_bystr = '-id'
    if order_by == 2:
        order_bystr = 'gprice'
    elif order_by == 3:
        order_bystr = '-gclick'
    list = typeinfo.goodsinfo_set.order_by(order_bystr)
    list_new = typeinfo.goodsinfo_set.order_by('-id')[0:2]
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
            plist = range(int(pindex)-2, int(plist)+3)

    context = {'title':'列表', 'cart':'1', 'type':typeinfo, 'list':page, 'plist':plist, 'new':list_new, 'order_by':order_by}
    return render(request, 'tt_good/list.html',context)


def detail(request, pid):
    try:
        # 根据传入的ID查询商品，搜索基数加1
        goods = GoodsInfo.objects.get(pk = pid)
        goods.gclick += 1
        goods.save()
        # 最新商品
        list_new = goods.gtype.goodsinfo_set.order_by('-id')[0:2]

        context = {'title':'详情', 'cart':'1','type':goods, 'new':list_new}
        response = render(request, 'tt_good/detail.html', context)
        # 查找最近浏览的数据存储结构id1,id2
        goods_ids = request.COOKIES.get('goods_ids', '')
        # 判断是否存在pid，如果存在删除，存到第一个，否则，直接加到第一个
        if len(goods_ids) == 0:
            goods_ids2 = [pid]
        else:
            goods_ids2 = goods_ids.split(',')
            if pid in goods_ids2:
                goods_ids2.remove(pid)
            else:
                if len(goods_ids2) >= 5:
                    goods_ids2.pop()
            goods_ids2.insert(0, pid)
        response.set_cookie('goods_ids', ','.join(goods_ids2))
        return response
    except:
        return render(request, '404.html')
