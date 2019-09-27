# num1=input('>>: ') #输入一个字符串试试
# int(num1)

# num1=input('>>: ') #输入一个字符串试试
# if num1.isdigit():
#     int(num1) #我们的正统程序放到了这里,其余的都属于异常处理范畴
# elif num1.isspace():
#     print('输入的是空格,就执行我这里的逻辑')
# elif len(num1) == 0:
#     print('输入的是空,就执行我这里的逻辑')
# else:
#     print('其他情情况,执行我这里的逻辑')

# s1 = 'hello'
# try:
#     int(s1)
# except Exception as e:
#     print(e)

# s1 = 'hello'
# try:
#     int(s1)
# except Exception as e:
#     # '丢弃或者执行其他逻辑'
#     print(e)

# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)

# class EvaException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
#
# try:
#     raise EvaException('类型错误----')
# except EvaException as e:
#     print(e)

# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)

# num=input("请输入数字：")
# if num.isdigit():
#     int(num)
# elif num.isspace():
#     print("不能为空格")
# elif len(num)==0:
#     print("没有输入任何内容")
# else:
#     print("其他")
#
# str=input("请输入数字:")
# try:
#     int(str)
# except Exception:
#     print("出现错误")
# except Exception as e:
#     print(e)
# str=input("请输入数字:")
# try:
#     int(str)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except:
#     print("其他")
# 自定义异常
# class dealError(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# try:
#     raise dealError("类型错误")
# except dealError as e:
#     print(e)
# str="zhangsan"
#
# try:
#     int(str)
# except Exception:
#     print(Exception.__dict__)
a = ["a1","a2"]
b=["b1","b2"]
c=[a,b]
li=dict(c)
print(li)