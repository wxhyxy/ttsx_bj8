# coding = utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^add/$', add),
    url('', cart),
    url('^cart_del/$', cart_del)
]