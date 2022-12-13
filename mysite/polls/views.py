from django.shortcuts import render
# 页面 --》处理层view --》数据库数据
# 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象
# 作为第一个参数，被“捕获”的参数以关键字参数的形式传入
from django.http import  HttpResponse
from polls.models import Question

def index(request):
    latest_qlist = Question.objects.order_by('-pub_date')[:5]
    output=','.join([q.question_text for q in latest_qlist])
    return  HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)