'''***********************删除文件夹
	必须保证当前文件夹为空才行
	需要把当前文件夹中所有文件 以及文件夹都删除
'''
import os
import sys
oriPath=os.path.join(os.getcwd(),"test")
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path,i)
        if os.path.isdir(c_path):
            if os.listdir(c_path)==[]:
                os.rmdir(c_path)
            else:
                del_file(c_path)
                os.rmdir(c_path)
        else:
            print(c_path)
            os.remove(c_path)

del_file(oriPath)

# ***********************把当前文件夹中的所有文件名字都获取到
# oriPath=os.path.join(os.getcwd(),"test")
# print(os.getcwd())
# def del_file(path):
#     ls = os.listdir(path)
#     for i in ls:
#         newPath = os.path.join(path,i)
#         if os.path.isdir(newPath):
#             if len(os.listdir(newPath))>0:
#                 del_file(newPath)
#         else:
#             print(newPath)
#
# del_file(oriPath)















