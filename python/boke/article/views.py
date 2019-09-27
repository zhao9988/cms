from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json,string,random
import pymysql
from datetime import datetime,timedelta
from common import common
from common import sqlconn

def list(request):
    uid = request.COOKIES.get('uid')
    print(uid)
    sql = "SELECT * FROM article WHERE uid = %s"
    data = uid
    print(uid)
    lis = sqlconn.db.select(sql, (1,), data)
    print("这是查询用户所有的文章的结果", lis)
    # 获取文章作者
    sql1 = "SELECT * FROM userinfo WHERE uid = %s"
    data1 = uid
    lis1 = sqlconn.db.select(sql1, (0,), data1)
    print("这是查询用户名的结果", lis1)
    li = []
    for item in lis:
        dic = item
        dic1 = {
            "uid": dic["uid"],
            "author": lis1["userName"],
            "writetime": datetime.strftime(dic["writetime"], "%Y-%m-%d %H:%M:%S"),
            "aid": dic["aid"],
            "title": dic["title"],
        }
        li.append(dic1)
        print("这是重新组成的字典", dic1)
    print("这是重新组成的列表", li)
    context={
        "data":li
    }
    print(context)
    response=render(request, "article/list.html", context)


    return response
# def listHandle(request):
#     uid = request.GET.get('uid')
#     print(uid)
#     sql="SELECT * FROM article WHERE uid = %s"
#     data=uid
#     print(uid)
#     lis = sqlconn.db.select(sql,(1,),data)
#     print("这是查询用户所有的文章的结果",lis)
#     # 获取文章作者
#     sql1="SELECT * FROM userinfo WHERE uid = %s"
#     data1=uid
#     lis1 = sqlconn.db.select(sql1,(0,),data1)
#     print("这是查询用户名的结果",lis1)
#     li=[]
#     for item in lis:
#         dic=item
#         dic1={
#             "uid":dic["uid"],
#             "author":lis1["userName"],
#             "writetime":datetime.strftime(dic["writetime"],"%Y-%m-%d %H:%M:%S"),
#             "aid":dic["aid"],
#             "title":dic["title"],
#         }
#         li.append(dic1)
#         print("这是重新组成的字典",dic1)
#     print("这是重新组成的列表",li)
#     return HttpResponse(common.returnData(0,"读取成功",li))
def add(request):
    tem = loader.get_template('article/add.html')
    context = {

    }
    return HttpResponse(tem.render(context, request))
def addHandle(request):
    title = request.POST.get('title')
    uid=request.POST.get('uid')
    content = request.POST.get('content')
    sql1 = "SELECT * FROM article WHERE  title= %s "
    data=(title)
    getData = sqlconn.db.select(sql1,(0,),data)
    print(getData)
    if (getData == None):
        msg="标题不存在"
        #将标题存入数据库
        sql2 = "INSERT INTO article (title,writetime,uid) values (%s,%s,%s)"
        time = datetime.now()
        data = (title, time, uid)
        sqlconn.db.query(sql2,(0,),data)
        # 获取存入标题的aid
        lastid=sqlconn.db.getLastId()
        print("这是新添加的文章的id",lastid)
        #将内容存入数据库
        sql4= "INSERT INTO articleContent (content,aid) values (%s,%s)"
        data2 = (content,lastid)
        sqlconn.db.query(sql4,(0,),data2)
    else:
        msg="标题已存在"

    response = HttpResponse(common.returnData(0,msg))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def articleDetail(request):
    tem = loader.get_template('article/articleDetail.html')
    context = {

    }
    return HttpResponse(tem.render(context, request))
def detailHandle(request):
    aid = request.GET.get('aid')
    print(aid)
    sql = "SELECT * FROM articlecontent WHERE aid = %s"
    date=(aid)
    lis = sqlconn.db.select(sql,(0,),date)
    print(lis)
    sql1="SELECT * FROM article WHERE aid = %s"
    lis1 = sqlconn.db.select(sql1,(0,),date)
    print(lis1)
    li = []
    dic1 = {
        "title":lis1["title"],
        "time": datetime.strftime(lis1["writetime"], "%Y-%m-%d %H:%M:%S"),
        "content": lis["content"]
    }
    li.append(dic1)
    print(dic1)
    print(li)
    response = HttpResponse(common.returnData(0,"进入detail页面",li))
    return response