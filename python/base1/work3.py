# f = open('file11',"r",encoding='utf-8')
# print(f.readline())
# print(type(f.readline()))
# print(f.readlines())
# f.seek(0)
# lis=f.readlines()
# print(lis)
# print(f.readable())     #判断文件是否可读
# print(f.writable())     #判断文件是否可写
# print(f.encoding)       #获取当前文件的编码格式
# print(f.tell())         #当前文件的指针指向
# f.seek(0)
# print(f.tell())         #当前文件的指针指向
# f.write("张三")
# f = open('text1.txt',encoding='utf-8') #默认只读模式
# print(f.read()) #可读
# f = open('file.txt','w',encoding='utf-8') #写模式
# f.write('test')#清空原有内容并写入
# # print(f.read()) #不可读，io.UnsupportedOperation: not readable
# f1 = open('file1.txt','w',encoding='utf-8')#f1不存,创建f1
# f = open('file.txt','r+',encoding='utf-8') #读写模式
# print(f.readable()) #可读
# print(f.writable())
# f.write("这是file文件")
# f1 = open('file1.txt','r+',encoding='utf-8')
# f1.write('bb') #能写，从文件开头写入覆盖，f1：aaaa， 写入后变为bbaa
# f2 = open('file2.txt','r+',encoding='utf-8')#f2不存，会报错
# f = open('file.txt','w+',encoding='utf-8') #写读模式
# # print(f.read()) #清空f，不会报错
# f.write("这是file文件")
# f1 = open('file1.txt','w+',encoding='utf-8')#f1为'aaaa'
# f1.write('bb') #清空原有内容并写入
# f2 = open('file2.txt','w+',encoding='utf-8')#f2不存,创建f2
# f = open('file.txt','a+',encoding='utf-8') #追加读写模式
# print(f.read()) #可读，但读取为空，追加读模式默认指针在文末
# f1 = open('file1.txt','a+',encoding='utf-8')#f1为'aaaa'
# f1.write('aaa') #可写，file1末尾追加写入‘bb'，f1为‘aaaabb’
# print(f1.read())
# f2 = open('file2.txt','a+',encoding='utf-8')#f2不存,创建f2
# f2.write("zzzzzzzzzzz")
# f = open('file.txt','r+',encoding='utf-8')
# print('f.readlines()',f.read());
# print('f.read',f.read())#读不到东西，因为read已经将文件指针指向文件末尾了

# f = open('file.txt','r+',encoding='utf-8')
# print('f.read',f.read())
# f.seek(0)
# print('f.read',f.read())#加入seek（0）后可以读到
# f = open('file.txt','r+',encoding='utf-8')
# for line in f:#读完一行的话，就会释放一行的内存
#     print(line)
# with open('file.txt','r+',encoding='utf-8') as f: #打开一个文件，把这个文件的句柄付给f
#     for line in f:
#         print(line)


# fw = open('file1.txt','a+',encoding='utf-8')
# fw.write('Amy')#有时写完，磁盘并未写入，原因是写入缓冲区，还未写入磁盘
# fw.flush() #强制把缓冲区里面的数据写到磁盘上

# f = open('file1.txt','a+',encoding='utf-8')
# f.seek(0)
# all_str = f.read()
# new_str = all_str.replace('78910','123456') #替换文件中的密码
# f.seek(0) #读完后，指针又指向文件末尾了，如果不重新seek，下面的清空文件不会清空指针之前的内容
# f.truncate()#清空文件内容
# f.write(new_str)
# f.close()

# f = open('file1.txt','a+',encoding='utf-8')
# f.seek(0)
# all_str = ''
# for line in f:
#     new_line = line.split('3')[-1] #将所有用户名前面的'syz_'去除
#     all_str += new_line
# f.seek(0)
# f.truncate()#清空文件内容
# f.write(all_str)
# f.close()

# import os
# with open('file1.txt',encoding='utf-8') as fr, open('file.txt','a+',encoding='utf-8') as fw:
#     for line in fr:
#         new_line = line.replace("z",'花')#读取原文件并替换
#         fw.write(new_line)#将替换后的内容写入新文件
# os.remove('file.txt') #删除原文件
# os.rename('file1.txt','file.txt') #重命名新文件

import os
# print(os.path.abspath('.'))
# path = os.path.join('./', 'testdir')
# print(path)
# print(os.path.split('/Users/michael/testdir/file.txt'))
# print(os.path.splitext('/path/to/file.txt'))
# os.rename('file.py', 'file.txt')
# 2.	编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。





