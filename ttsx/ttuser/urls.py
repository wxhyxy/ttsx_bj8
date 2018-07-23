# coding = utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^register/$', regisger),
    url('^register_handle/$', register_handle),
    url('^login/$', login),
    url('^register_valid/$', register_valid),
    url('^login_handle/', login_handle),
    url('^login_out/$', login_out),
    url('^center/$', center),
    url('^order/$', order),
    url('^site/$', site),
    url('^area/$', area),
    url('^area1_(\d+)/', area1),
    url('^islogin/$', islogin),
]