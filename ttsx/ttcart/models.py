# coding=utf-8
from django.db import models
from ttuser.models import *
from ttgood.models import *

# Create your models here.
class CartInfo(models.Model):
    # 关联用户和商品,和数量
    cuser = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    cgood = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    ccoumt = models.IntegerField()