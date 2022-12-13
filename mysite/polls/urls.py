# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 20:00
# @Author  : alvin
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]