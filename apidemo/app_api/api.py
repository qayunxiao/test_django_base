from django.shortcuts import render

# Create your views here.

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
api = NinjaAPI()
@api.get("/add")
# http://127.0.0.1:8000/api/add?a=1&b=2
def add(request, a: int, b: int):
    return {"result": a + b}

@api.api_operation(["GET","PUT","DELETE"],"/user/")
def user(request,user_id:int):
    print("method",request.method)
    print("user_id",user_id)
    if request.method == "GET":
        return {"result":"get user info"}
    if request.method == "PUT":
        return {"result":"update user info"}
    if request.method == "DELETE":
        return {"result":"delete user info"}


