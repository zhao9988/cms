from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.
def register(request):
    tem=loader.get_template('user/register.html')
    context={

    }
    return  HttpResponse(tem.render(context,request))

def registerHandle(request):
    username = request.POST.get('username')
    response = HttpResponse(username)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def login(request):
    tem = loader.get_template('user/login.html')
    context = {

    }
    return HttpResponse(tem.render(context, request))
def loginHandle(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    # if username == "zhangsan" and pwd =="123":
    #     data={
    #         "code":0,
    #         "msg":"登陆成功"
    #     }
    # else:
    #     data = {
    #         "code": 1,
    #         "msg": "登陆失败"
    #     }
    response = HttpResponse("登陆成功")
    response["Access-Control-Allow-Origin"] = "*"
    return response