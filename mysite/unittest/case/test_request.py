# -*- coding: utf-8 -*-
# @Time    : 2022/12/17 16:36
# @Author  : alvin
# @File    : test_request.py
# @Software: PyCharm
import  requests
r= requests.get("http://127.0.0.1:8080/polls/")
print(r.status_code)