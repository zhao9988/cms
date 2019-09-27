from django.shortcuts import render
# Create your views here.
from example1.models import *
from django.http import HttpResponse
def show_class(request):
    # class_list =article.objects.all().order_by('articleId')
    article.objects.filter(articleId=3).delete()
    return render(request, 'example1/exp.html')
def login(request):
    response= render(request,'index.html', {})
    response.set_cookie('my_cookie',66,max_age=60 * 60 * 24 * 7)
    return response

def index(request):
    #提取游览器中的cookie，如果不为空，表示为已登录帐号
    v = request.COOKIES.get('uid')
    return render(request,'index.html',{'uid':v})

# def setSession(request):
    # request=request.GET.get("uid")
    # request.session['key'] = 333
    # return render(request, 'setSession.html', {})
def getSession(request):
    # request=request.GET.get("uid")
    # request.session['key'] = 123
    # a=request.session['key']
    # print(a)
    # request.session.delete()
    # del request.session['key']
    # del request.session['key']
    request.session.flush()
    return render(request, 'getSession.html')