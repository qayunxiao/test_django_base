"""apidemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]