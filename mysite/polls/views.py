from django.shortcuts import render
# 页面 --》处理层view --》数据库数据
# Create your views here.
from django.http import  HttpResponse

def index(request):
    return  HttpResponse("Hello,world ,polls page")