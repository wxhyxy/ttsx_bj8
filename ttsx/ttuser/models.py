from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)

    ushou = models.CharField(max_length=10,null=True)
    uaddr = models.CharField(max_length=100, null=True )
    uphone = models.CharField(max_length=11, null=True)

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=40)
    aPentar = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True)