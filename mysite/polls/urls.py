# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 20:00
# @Author  : alvin
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index)
]