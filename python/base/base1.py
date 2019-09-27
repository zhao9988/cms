import string
import random
import json
import os
from datetime import date
from datetime import datetime

# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.printable)
# print(string.punctuation)
# print(string.hexdigits)
#字母和数字的验证码
# def security():
#     num=random.sample(string.ascii_letters+string.digits,4)
#     print("".join(num))
# security()
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# str_dic = json.dumps(dic)  #序列化：将一个字典转换成一个字符串
# print(type(str_dic),str_dic)
# dic2 = json.loads(str_dic)
# print(type(dic2),dic2)
# f = open('json_file','w')
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# json.dump(dic,f)  #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
# f.close()
#
# f = open('json_file')
# dic2 = json.load(f)  #load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
# f.close()
# print(type(dic2),dic2)

# now=date.today()
# print(now)
# print(now.strftime("%Y.%m.%d"))
# print(now.strftime('%Y{}%m{}%d{}').format("年","月","日"))
# birthday=date(2000,1,1)  #构造一个date对象，参数：年、月、日
# print(birthday)
# age=now-birthday
# print(age)  #7158 days, 0:00:00
# print(age.days)
# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# print(dt)

# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# ts=dt.timestamp() # 把datetime转换为timestamp
# print(ts)
# t = 1429417200.0
# print(datetime.fromtimestamp(t))

# from datetime import datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)


# import xml.sax
# class MovieHandler(xml.sax.ContentHandler):
#
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""
#     # 元素开始事件处理
#
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "movie":
#             print("*****Movie*****")
#             title = attributes["title"]
#             print("Title:", title)
#     # 元素结束事件处理
#     def endElement(self, tag):
#         if self.CurrentData == "type":
#             print("Type:", self.type)
#         elif self.CurrentData == "format":
#             print("Format:", self.format)
#         elif self.CurrentData == "year":
#             print("Year:", self.year)
#         elif self.CurrentData == "rating":
#             print("Rating:", self.rating)
#         elif self.CurrentData == "stars":
#             print("Stars:", self.stars)
#         elif self.CurrentData == "description":
#             print("Description:", self.description)
#         self.CurrentData = ""
#     # 内容事件处理
#     def characters(self, content):
#         if self.CurrentData == "type":
#             self.type = content
#         elif self.CurrentData == "format":
#             self.format = content
#         elif self.CurrentData == "year":
#             self.year = content
#         elif self.CurrentData == "rating":
#             self.rating = content
#         elif self.CurrentData == "stars":
#             self.stars = content
#         elif self.CurrentData == "description":
#             self.description = content
#
# if (__name__ == "__main__"):
#     #make_parser
#     # parser = xml.sax.make_parser()
#     # parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#     # Handler = MovieHandler()
#     # parser.setContentHandler(Handler)
#     # parser.parse("xml1.xml")
#
#
#     #parser
#     Handler = MovieHandler()
#     xml.sax.parse( "xml1.xml", Handler)
#


# now=datetime.now()
# dt=now.strftime("%Y-%m-%d %H:%M:%S")
# print(dt)
# dt=now.strftime("%Y-%m-%d")
# print(dt)
# date1=datetime(2019,8,20,10,10,10)
#
# dt=date1.timestamp()
# print(dt)
# str="2019-8-8 10:10:10"
# time1=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
# print(time1)
# str = "2019-9-8 10:10:10"
# time1=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
# time2=time1.timestamp()
# print(time1)
# print(time2)


