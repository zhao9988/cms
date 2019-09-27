# ***********************删除文件夹
# import os
# oriPath=os.path.join(os.getcwd(),"test")
# def func_del(path):
#     if os.path.exists("test"):
#         if os.path.isdir(path):
#             lis=os.listdir(path)
#             print(lis)
#             for i in lis:
#                 newPath=os.path.join(path,i)
#                 if os.path.isdir(newPath):
#                     if len(os.listdir(newPath))>0:
#                         func_del(newPath)
#                     else:
#                         os.rmdir(newPath)
#                 else:
#                     os.remove(newPath)
#             else:
#                 os.rmdir(path)
#         elif os.path.isfile(path):
#             os.remove(path)
#     else:
#         print("test不存在")
# func_del(oriPath)
import os
def delDir(dir):
    # 判断传递过来的dir是否存在
    if not os.path.exists(dir):
        print("当前目录不存在")
        return
    if os.path.exists(dir):
            # 判断当前dir是文件还是文件夹
        if os.path.isfile(dir):
            # 当前是文件
            print("文件",dir)
            os.remove(dir)
            return
        # 当前是文件夹
        # 判断当前文件夹是否为空
        dirlist=os.listdir(dir)
        if len(dirlist)==0:
            print("文件夹是空",dir)
            # 删除空的文件夹
            os.rmdir(dir)
            return
        # 当前文件夹非空
        print("文件夹非空")
        for item in dirlist:
            # 查看当前item是文件还是文件夹
            itemPath = os.path.join(dir, item)
            # itemPath = item
            if os.path.isfile(itemPath):
                # 当前是文件 相对于当前文件所在的目录去查找item
                # 查找到item的绝对路径
                print("其中包含文件",itemPath)
                os.remove(itemPath)
            else:
                #查找到了是文件夹
                print("其中包含文件夹", itemPath)
                delDir(itemPath)
        else:
            os.rmdir(dir)
path=os.path.join(os.getcwd(),"test")
print(path)
delDir(path)

















