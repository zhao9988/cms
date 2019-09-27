from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.

def list(request):
    tem = loader.get_template('article/list.html')
    context = {

    }
    return HttpResponse(tem.render(context, request))
def add(request):
    tem = loader.get_template('article/add.html')
    context = {

    }
    return HttpResponse(tem.render(context, request))
def addHandle(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        response = HttpResponse(content)
        response["Access-Control-Allow-Origin"] = "*"
        return response

def articleDetail(request):
    tem = loader.get_template('article/articleDetail.html')
    context = {

    }
    return HttpResponse(tem.render(context, request))