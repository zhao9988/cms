# # 求当前时间到2019年8月24日 差___天___小时____分钟___秒
from datetime import datetime
# time1=datetime(2019,8,24)
# mrotime1=datetime.timestamp(time1)
# time2=datetime.now()
# mrotime2=datetime.timestamp(time2)
# difmrotime=mrotime1-mrotime2
# # print(difmrotime)
# timeday=difmrotime/60/60/24
# # print(timeday)
# day=int(timeday)
# difDay=timeday-day
# timehour=difDay*24
# # print(timehour)
# hour=int(timehour)
# difHour=timehour-hour
# # print(difHour)
# timeMinutes=difHour*60
# # print(timeMinutes)
# minutes=int(timeMinutes)
# difMinutes=timeMinutes-minutes
# # print(difMinutes)
# timesecond=difMinutes*60
# # print(timesecond)
# second=int(timesecond)
# print("到2019年8月24日还差%s天%s小时%s分钟%s秒"%(day,hour,minutes,second))

# time1=datetime(2019,8,23,12,30)
# time2=datetime.now()
# diftime=time1-time2
# timeHour=diftime.seconds/60/60
# hour=int(timeHour)
# difMinutes=timeHour-hour
# timeMinutes=difMinutes*60
# minutes=int(timeMinutes)
# difSecond=timeMinutes-minutes
# timeSecond=difSecond*60
# second=int(timeSecond)
# print("到2019年8月23日12点还差%s天%s小时%s分钟%s秒"%(diftime.days,hour,minutes,second))
# import os
# filesList=[]
# def getFilesName(path):
#     global filesList
#     print(path)
#     if not os.path.exists(path):
#         print("当前文件/文件夹不存在")
#         return
#     if os.path.isfile(path):
#         print("文件")
#         filesList.append(path)
#         return
#     dirList=os.listdir(path)
#     if dirList==[]:
#         print("文件夹是空的文件夹")
#         return
#     for item in dirList:
#         # 得到item的完整的路径
#         itemPath=os.path.join(path,item)
#         if os.path.isfile(itemPath):
#             print("item是文件")
#             filesList.append(item)
#         else:
#             print("item是文件夹")
#             getFilesName(itemPath)
#
#
#
# path=os.path.join(os.getcwd(),"test2")
# getFilesName(path)
# print(filesList)

import os
def search_file(path, str):  # 传入当前的绝对路径以及指定字符串
    # 首先先找到当前目录下的所有文件
    for item in os.listdir(path):  # os.listdir(path) 是当前这个path路径下的所有文件的列表
        this_path = os.path.join(path, item)
        if os.path.isfile(this_path):  # 判断这个路径对应的是目录还是文件，是文件就走下去
            if str in this_path:
                print(this_path)
        else:   # 不是就再次执行这个函数，递归下去
            search_file(this_path, str)  # 递归下去
    else:
        return

path=os.path.join(os.path.abspath("."),"test")
search_file(path, "test12")













