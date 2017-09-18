#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return render(requset,'blog/index.html',context={
        'title': '小果子的博客首页',
        'welcome': '欢迎访问小果子的博客首页'
    })
