# coding = utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^register/$', regisger),
    url('^register_handle/$', register_handle)
]