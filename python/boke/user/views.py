from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pymysql
from common import common
from common import sqlconn
# Create your views here.



# 建立数据库连接
def register(request):
    tem=loader.get_template('user/register.html')
    context={

    }
    return  HttpResponse(tem.render(context,request))
def registerHandle(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    sql="SELECT * FROM userinfo WHERE userName = %s"
    data=username
    getUserInfoFromDB=sqlconn.db.select(sql,(0,),data)
    # print(getUserInfoFromDB)
    if getUserInfoFromDB == None:
        key = "userName,pwd"
        val="%s,%s"
        data1=(username,pwd)
        if email:
            key += ",email"
            val += ",%s"
            data1 = (username, pwd, email)
        sql1="INSERT INTO userinfo("+key+")VALUES("+val+")"
        try:
            getUserInfoFromDB = sqlconn.db.query(sql1, (0,), data1)
            return HttpResponse(common.returnData(0, "注册成功"))
        except Exception as e:
            return HttpResponse(common.returnData(1, "注册失败"))
    return HttpResponse(common.returnData(1, "注册失败,用户名已存在"))
def login(request):



    return render(request,"user/login.html")

def loginHandle(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    print(username,pwd)
    sql = "SELECT  uid,pwd FROM userinfo WHERE userName = %s"
    data=(username)
    getUserInfoFromDB=sqlconn.db.select(sql,(0,),data)
    print(getUserInfoFromDB)
    print(getUserInfoFromDB["uid"])
    if getUserInfoFromDB:
        # 此时用户名存在
        if pwd == getUserInfoFromDB["pwd"]:
            uid=getUserInfoFromDB["uid"]
            response=HttpResponse(common.returnData(0, "登录成功"))
            response.set_cookie("uid",uid,max_age=60*60*24*7)
            return  response
        return HttpResponse(common.returnData(1, "登陆失败，密码不正确"))
    else:
        return HttpResponse(common.returnData(1, "登陆失败，用户不存在"))


