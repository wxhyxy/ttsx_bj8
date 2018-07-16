# coding = utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', index),
    url('^list(\d+)$', list_goods)
]