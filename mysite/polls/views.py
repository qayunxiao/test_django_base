from django.shortcuts import render
# 页面 --》处理层view --》数据库数据
# 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象
# 作为第一个参数，被“捕获”的参数以关键字参数的形式传入
from django.http import  HttpResponse

def index(request):
    return  HttpResponse("Hello,world ,polls page")