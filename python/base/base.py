'''
这是第一个python基础文件
'''
# print("hello world!")

# 声名变量

#变量命名规则:变量名是字母数字下划线的任意组合,变量名第一个字符不能是数字，变量名不能是关键字(eg:if)

# name="赵君霞"
# print(name)

# 驼峰式命名
# firstName="赵君霞111"
# print(firstName)

# 下划线命名
# first_name="赵君霞222"
# print(first_name)

# 程序交互
# name = input("请输入用户名：")
# print(name)

# name = input("What is your name?")
# age = input("How old are you?")
# hometown = input("Where is your hometown?")
# print("Hello ",name , "your are ", age , "years old, you came from",hometown)

# 数据类型
# name="赵君霞"
# print(type(name))
# <class 'str'>

# age=20
# print(type(age))
# <class 'int'>

# age=20.1
# print(type(age))
# <class 'float'>

# msg = '''
# 今天我想写首小诗，
# 歌颂我的同桌，
# 你看他那乌黑的短发，
# 好像一只炸毛鸡。'''
# print(msg)

# msg = "今天我想写首小诗，歌颂我的同桌，你看他那乌黑的短发，好像一只炸毛鸡。"
# print(msg)

# 字符串的拼接只能是双方都是字符串
# name='Bingbing fan'
# age='222222222'
# print(name+age)
# Bingbing fan222222222

# name='赵君霞'
# age=2
# print(name*age)
# 赵君霞赵君霞

# a=3
# b=5
# print(a>b)
# False
# print(b>a)

# name="zhao"
# print(name=="zhao")
# True

# 格式化输出


# name = input("Name:")
# age = input("Age:")
# job = input("Job:")
# hobbie = input("Hobbie:")
#
# info = '''
# Name  : %s
# Age   : %s
# job   : %s
# Hobbie: %s------------- end -----------------''' %(name,age,job,hobbie)
# print(info)


# age = input("Age:")           会报错
# age = int(input("Age:"))
# print(type(age))
# info = '''
# Age   : %d
# ''' %(age)
# print(info)

# %用来转译
# msg = "我是%s,年龄%d,目前学习进度为80%%"%('赵君霞',18)
# print(msg)

# print(3>4 or 4<3 and 1==1)
# False

# print(1 < 2 and 3 < 4 or 1>2 )
# True

# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# True

# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# False

# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# False

# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# False

# print('喜欢' in 'dkfljadklf喜欢hfjdkas')
# print('喜欢' not in 'dkfljadklf喜欢hfjdkas')

# num=2.1
# print(int(num))

# str="2"
# print(int(str))

# num=2
# print(float(num))

# str="2.212222"
# print(float(str))

# num=2.11
# print(str(num))

# chr输入一个数字，返回的是在ASCII表中十进制数值为此数字的值
# num=chr(121)
# print(num)
# -------y

# 输入一个字符，返回的是在ASCII表中对应的十进制数值
# str=ord("z")
# print(str)
# ----122

# age=20
# if age==20 :
#     print("你今年20岁啦！")

# age=18
# if age>18 :
#     print("你已经成年了！")
# elif age == 18 :
#     print("你今年成年了！")
# else:
#     print("你还未成年")


# break让程序跳出count +=1的循环
# count = 0
# while count <= 100 : #只要count<=100就不断执行下面的代码
#     print("loop ", count)
#     if count == 5:
#         break
#     count +=1 #每执行一次，就把count+1，要不然就变成死循环啦，因为count一直是0
# print("-----out of while loop ------")

# count = 0
# while count <= 100 :
#     count += 1
#     if count > 5 and count < 95: #只要count在6-94之间，就不走下面的print语句，直接进入下一次loop
#         continue
#     print("loop ", count)
# print("-----out of while loop ------")

# count = 0
# while count <= 5 :
#     count += 1
#     print("Loop",count)
# else:
#     print("循环正常执行完啦")
#     print("-----out of while loop ------")

# count = 0
# while count <= 5 :
#     count += 1
#     if count == 3:
#         break
#         print("Loop",count)
#     else:
#         print("循环正常执行完啦")
#         print("-----out of while loop ------")


# 作业

# 1、使用while循环输出 1 2 3 4 5 6 8 9 10

# num=0
# while num<10 :
#     num+=1
#     print(num)

# 2、求1-100的所有数的和
# num=1
# sum=0
# while num<101 :
#     sum += num
#     num+=1
#     print(sum)

# 3、输出 1-100 内的所有奇数
# num=1
# while num<101:
#     if num%2==1:
#         print(num)
#     num+=1

# 4、输出 1-100 内的所有偶数
# num=1
# while num<101:
#     if num%2==0:
#         print(num)
#     num+=1

# 5、求1-2+3-4+5 ... 99的所有数的和
# num=0
# sum=0
# while num<100:
#     if num%2==1:        #此时为奇数
#         sum+=num
#     else:
#         sum -= num
#     num+=1
# print(sum)

# 6. 写个猜年龄的游戏
# 	先定义一个变量 age=23;
# 	再定义一个变量 age1，此值为用户输入得到的
# 	如果用户输入的age1的值不为age的值就让用户一直输入，提示：“猜错了，您还剩下xxx次机会!”，
# 	如果输入的次数超过了三次就不让用户输入了，提示：次数用尽；如果在三次以内
# 	输入正确就输出“在三次之内猜对了年龄！”
# age=23
# age1=int(input("请输入年龄"))
# num=1
# while num<4:
#     if age1!=age:
#         print("猜错了，您还剩下",(3-num),"次机会!")
#         age1 = int(input("请输入年龄"))
#         num+=1
#         if (3-num)==0:
#             print("次数用尽")
#             break
#     else:
#         print("在三次之内猜对了年龄！")
#         break


# a = 'ABCDEFGHIJK'
# print(a[4])
# 输出的是此字符串中索引值为4的字符

# a = 'ABCDEFGHIJK'
# print(a[0:3])
# print(a[0:])
# print(a[0:-2])
# 从索引0到倒数第2个,倒数第二个取不到
# print(a[0:5:2]) #加步长
# 从索引值0取到5,每两个取一个   0,2,4
# print(a[5:0:-2])
# 从索引值5处取到索引值0,每次向前取两个,即5,3,1
# print(a.capitalize())
# a.capitalize()
# a="AkdjHSJS"
# print(a.swapcase())

# msg='tom say hi'
# print(msg.title())
# ret2 = msg.center(20,"*")
# print(ret2)

# ret3 = msg.count("a",0,6) # 可切片
# print(ret3)

# print(msg.startswith("t"))
# print(msg.startswith("t",1,2))
# print(msg.endswith("i"))

# print(msg.find("b"))#找不到返回-1
# print(msg.find("m",0,3))

# print(msg.index("t"))#找不到则报错,找到返回索引值

# ret9 = 'titleTilteatre,'.split('t')#以"t"分割,从前往后
# print(ret9)
# ret91 = 'titleTilteatre,'.split('t',1)#以前一个"t"分割,从前往后
# print(ret91)
# ret92 = 'titleTilteatre,'.rsplit('t',1)#以最后一个"t"分割,从后往前
# print(ret92)

# res='{} {} {}'.format('tom',18,'male')
# print(res)

# res='{1} {0} {1}'.format('lili',18,'male')
# print(res)
#显示索引值为1处的内容,显示索引值为0处的内容,显示索引值为1处的内容

# res='{name} {age} {sex}'.format(sex='male',name='liu',age=18)
# print(res)

# name='*marry**'
# print(name.strip('*'))
# print(name.lstrip('*'))
# print(name.rstrip('*'))

# name='tom say :i have one tesla,my name is tom'
# print(name.replace('tom','marry',1))
# 以marry替换tom,只替换一次,默认全部替换

# name='tanyueling123'
# print(name.isalnum()) #字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成
# print(name.isdigit()) #字符串只由数字组成

# print(8 or 4)
# print(0 and 3)
# print(0 or 4 and 3 or 7 or 9 and 6)
# print(0 or 4 )
# print(3 or 7 or 9)
# print(4 and 3 and 9)

#元组
# tul=(1,2,3,4,5,6)
# tul=tuple((1,2,3,4))
# print(len(tul))
# print(tul.count(3))
# print(tul.index(4))
# print(tul[0])
# print(tul[-1])
# print(tul[1:3])
# print(tul[:-1])
# print(tul[::2])
# print(tul[::-1])

#遍历元组
# for i in tul:
#     print(i)

#列表     list
# li = [1,'a','b',2,3,'a']
# li.insert(0,"zhao")
# li.append("zhao")
# li.extend(['q,a,w']) #迭代的去增
# li.extend(['q,a,w','aaa'])
# li.extend('a')
# li.extend('abc')
# li.extend('a,b,c')
# l1=li.pop(2)
# del li[1:3]
# del li[1:3]
# li.remove("a")      #一次只能删除一个
# li.clear()
# li[1]="c"
# li[1:5] = ['a','c']
# print(li)
# print(l1)
#遍历列表
# for i in li:
#     print(i)

# a = ["q","w","q","r","t","y"]
# print(a.count("q"))
# print(a.index("q"))
# a=[0,1,5,3,2,8,7]
# a.sort()
# a.reverse()
# print(a)
# dic={
#
# }
# dic['li'] = ["a","b","c"]
# dic["zhao"]="zhao"
# dic.setdefault('k', 'v')
# dic.setdefault("li","zao")
# print(dic)
# dic_pop = dic.pop("li",'字典中没有此键')
# print(dic_pop)
# del dic["li"]
# dic_pop1 = dic.popitem()
# print(dic_pop1)
# dic_clear = dic.clear()  # 清空字典
# print(dic_clear)  #None
# dic = {"name":"zhao","age":18,"sex":"male"}
# dic2 = {"name":"wu","weight":75}
# dic2.update(dic)  # 将dic所有的键值对覆盖添加（相同的覆盖，没有的添加）到dic2中
# print(dic2)
# dic1={"name":"wu"}
# dic.update(dic1)
# value1 = dic["name"]  # 没有会报错
# print(value1)
# value2 = dic.get("name","默认返回值")  # 没有可以返回设定的返回值
# print(value2)
# item = dic.items()
# print(len(item))
# print(item,type(item))
# keys = dic.keys()
# print(keys,type(keys))
# values = dic.values()
# print(values,type(values))
# print(dic)

#字典的循环
# dic = {"name":"zhao","age":18,"sex":"male"}
# for item in dic:
#     print(item)
# for key in dic:
#     print(key)
# for key,value in dic.items():
#     print(key,value)
# for key in dic.items():
#     print(key)

# set1={2,2,3,4,5,6,7}
# set1=set({1,2,3})
# set1.add("jasjdasfna按面积收费咖啡")
# set1.update('A')
# print(set1)
# set1.update('张三')
# set1.update("akjsfja","asad")
# set1.update([4,5,6])
# set1.remove(2)  # 删除一个元素

# set1.pop()
# set1.clear()
# del set1

# print(set1)

# 作业：
# 1.	同时输入5名同学的姓名，性别，年龄和成绩，最后把所有同学的信息再按照每人一行的格式输出显示
# num=0
# list=[]
# while num<5:
#     name = input("姓名:")
#     gender = input("性别:")
#     age = input("年龄:")
#     score = input("成绩:")
#     dict = {
#         "name": name,
#         "gender": gender,
#         "age": age,
#         "score": score
#     }
#     list.append(dict)
#     num+=1
# for item in list:
#     info='''姓名为%s,性别为%s,年龄为%s,成绩为%s'''%(item["name"],item["gender"],item["age"],item["score"])
#     print(info)
# 2.	获取100以内的所有质数并把它们都放入列表中存储
# list=[2]
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#         elif i==j+1:
#             # print(i)
#             list.append(i)

# for i in range(2, 100):
#    for j in range(2, i):
#         if i % j == 0:
#             break
#    else:
#         list.append(i)
#         print(i)
# print(list)
# 3.	使用字典来存储 校名，建校时间，人数，地址，其中地址这个属性所对应的值的类型为对象，又包括属性：国家，城市
# schoolName=input("校名为:")
# builtTime=input("建校时间为:")
# peopleNun=input("人数为:")
# country=input("国家为:")
# city=input("城市为:")
# address={
#     "country":country,
#     "city":city
# }
# dic={
#     "schoolName":schoolName,
#     "builtTime":builtTime,
#     "peopleNun":peopleNun,
#     "address":address
# }
# dic={'schoolName': 'NCIST','builtTime': '1970', 'address': {'country': 'china', 'city': 'langfang'},  'peopleNun': '3000'}
# print(dic)

# 4.	再通过for循环来获取上面2题 和3题中的所有数据

# for i in list:
#     print(i)

# for key,value in dic.items():
#     if type(value)==dict :
#         for key,value in value.items():
#             print(value)
#     else:
#         print(value)

#函数
# def func_name1():
#     print("hello world")
# func_name1()
#带参数的函数
# def func_name1(name):
#     print("my name is :",name)
# func_name1('zhao')
#位置参数
# def func_name2(a,b):
#     c=a*b
#     print(c)
#
# func_name2(2,3)
#关键字参数
# def func_name2(a,b):
#     c=a*b
#     print(c)
#
# func_name2(a=2,b=3)
#带有return的函数        遇到return就结束函数，所以不管一个函数里有多少return，return返回的值都是第一个return返回的值
# def with_return(a,b):
#     return (a * b)
#     return(a + b)

# print(with_return(a=2,b=3))

#在函数体内为全局变量赋值

# name,age="alex",20      #全局变量
# print(name,age)
# def func_name():
#     global name     #局部变量
#     global age      #局部变量
#     name = 'oldboy'
#     age=100
#     print(name)
#     print(age+1)
# func_name()
# print(name,age)
#非固定参数*args,传入的值自动转化为元组，元组可为空
# def func_name5(name,age,*args):
#     print(name,age,args)
#
# func_name5("zhao",20,"女")
#非固定参数*kwargs，传入的是key=value,传入函数后自动转化为字典，字典也可为空
# def func_name5(name,age,**kwargs):
#     print(name,age,kwargs)
#
# func_name5('alex',18,gender="女")

# def func_name7(name,age,*args,**kwargs):
#     print(name,age,kwargs,args)
#
# func_name7("zhao", 20,"studengt",gender="女",sex="女", gen="女")

# 作业：
# 1．写一个函数，接收参数n,输出n个hello word

# def hello(n):
#     str="hello word! "*n
#     print(str)
# hello(3)

# 2. 定义一个函数，接收三个参数num1,num2，以及符号"+","-","X","/","%",函数的内容是对符号进行判断之后，再进行计算，并且把得到的结果返回。

# def count(num1,num2,symbol):
#     if symbol=="+":
#         return num1+num2
#     elif symbol=="-":
#         return num1 - num2
#     elif symbol == "*":
#         return num1 * num2
#     elif symbol=="/":
#         return num1 / num2
#     elif symbol=="%":
#         return num1 % num2
#     else:
#         return ("请输入正确的运算符")
# print(count(9,3,"+"))

# 3. 定义一个函数，接收两个参数num1,num2,函数的内容是计算两个数字的和，如果num1>num2就把两个数字的和返回，反之就不做任何处理。

# def sum(num1,num2):
# #     if num1>num2:
# #         return num1+num2
# #
# # print(sum(2,5))

# 4.定义一个函数，接收一个参数num,函数的内容为判断当前num是否为质数，如果是质数，此函数返回 true   如果不是质数此函数返回false

# def jude(num):
#     num1=2
#     while num1<num:
#         if num%num1==0:
#             return "false"
#         num1+=1
#     else:
#         return "true"
#
# print(jude(12))


#匿名函数
# s =lambda x,y:x+y
# print(s(1,9))

# s =lambda x:"当前输入的为"+str(x)
# print(s(1))

# 通过sorted对字典排序：

# d = {'a':1,'b':2,'c':3}
# print(d.items())
# res = sorted(d.items())
# print(res)
#以key的值排序
# res1 = sorted(d.items(),key=lambda x:x[0])
# print(res1)
#以value的值反转排序
# res2 = sorted(d.items(),key=lambda x:x[1],reverse=True)
# print(res2)
# for k,v in res2:
#     print(k,v)

# 内置函数

# print(round(11.23454,2))#四舍五入保留几位小数
# dic={}
# print(id(dic)) #看内存地址
# print(type(dic)) #看数据类型
# str="ABCD"
# list = list(str)
# print(str)
# print(list)
# print(dir('abc'))

# print(dir())
# print(dir({}))#打印传入对象的可调用方法

# print(all([1,2,3,4]))

# print(bool(""))

# a=filter(lambda  x: x > 5, [12, 3, 12, 2, 1, 2, 35])

# print(list(a))

# print(map(lambda x: x > 5, [1, 2, 3, 4, 5, 6]))
# print(list(map(lambda x: x > 5, [1, 2, 3, 4, 5, 6])))

# def a(n,m):
#     print(n,m)
# a(1,m=4)

# class Money:
#     pass
#
# one = Money()
# print(type(Money))
# print(type(one))
# print(Money.__name__)  # 访问类的名称
# print(one.__class__)  # 访问实例对应的类
# print(one.__class__.__name__)
# print(Money.__name__)
# print(Money.__dict__)

# a = 10
# print(type(a))

# xxx = type('dog', (), {'count': 0})
# print(xxx)

# class money:
#     age = 19
#     num = 123  # 直接在类中添加属性
#
#
# money.count = 1  # 给类增加一些属性，类属性=值
# money.age = 3  # 给类的属性直接赋值；来改变属性值
# print(money.count)
# print(money.age)
# print(money.__dict__)

# class Person:
#     pass
#
# p = Person()

# 给p对象增加一些属性，对象属性=值
# p.age = 18
# # 验证是否有添加成功
# print(p.age)
# print(p.__dict__)  # 查看对象的所有属性，以字典形式返回
# print(Person.__dict__)      #并没有
# p.age = [1, 3]  # 修改操作，直接赋值修改对象的属性，id会变
# print(p.age)
# p.age.append('小花')  # 访问操作，操作（添加）值，id不变
# print(p.age)

# class person:
#     __slots__ = ['age']  # 限制对象属性的添加
#     pass
#
# p1 = person()
# p1.age = 10
# p1.num=10 #报错AttributeError: 'person' object has no attribute 'num'
# print(p1.age)


# class Animal:
#     __x = 10
#
#     def test(self):
#         print(Animal.__x)
#         print(self.__x)
#
#
# print(Animal.__dict__)
# print(Animal._Animal__x)

# class Person:
#     def __init__(self):
#         self.__age = 18
#
#     def getAge(self):
#         return self.__age
#
#     @property  # 可以将一些属性的操作方法关联这个方法,修饰的是age
#
#     def age(self):
#         return self.__age
#
# p = Person()
# print(p.getAge())
# print(p.age)

# class Person:
#     def __setattr__(self, key, value):
#         print(key, value)
#         if key == 'age' and key in self.__dict__.keys():
#             print('只读属性')
#         else:
#             self.__dict__[key] = value
#
# p = Person()
# p.age = 19
# p.name = 'sz'
# print(p.__dict__)
# print(p.age)
# p.age = 12
# print(p.age)

# class person:
#     def __init__(self):
#         self.__age = 18
#
#     def setAge(self, value):
#         if isinstance(value, int) and 0 < value < 200:  # 数据过滤
#             self.__age = value
#         else:
#             print('数据错误')
#
#     def getAge(self):
#         return self.__age
#
# p = person()
# print(p._person__age)
# p.setAge(20)
# print(p._person__age)
# print(p.getAge())


# class Person:
#     def __init__(self):
#         self.name="zhao"
#         self.__age=10
# p=Person();
# print(p._Person__age)
# print(p.age)


# class Person:
#     def __init__(self):
#         self.__age = 18
#
#
#     def getAge(self):
#         return self.__age
#
#
#     @property  # 可以将一些属性的操作方法关联这个方法
#     # property(fget=Nofne, set=None, fdel=None, doc=None)
#     def Age(self):
#         print("这是age函数")
#         return self.__age
#
# p = Person()
# p.Age=666
# print(p.getAge())
# print(p.Age)

# class Person:
#     def __setattr__(self, key, value):
#         # print(key, value)
#         if key == 'age' and key in self.__dict__.keys():
#             print('只读属性')
#         else:
#             self.__dict__[key] = value
#
# p = Person()
# print(p.__dict__)
# p.age = 19
# p.name = 'sz'
# print(p.__dict__)
# print(p.age)
# p.age = 12
# print(p.age)

# print(isinstance("zhangsan",int))
# class Person:
#     pass
#
#
# p = Person()
#
# # 给p对象增加一些属性，对象属性=值
# p.age = 18
# # 验证是否有添加成功
# print(p.age)
# print(p.__dict__)  # 查看对象的所有属性，以字典形式返回
#
# p.age = [1, 3]  # 修改操作，直接赋值修改对象的属性，id会变
# print(p.age)
#
# p.age.append('小花')  # 访问操作，操作（添加）值，id不变
# print(p.age)

# class person:
#     __slots__ = ['age']  # 限制对象属性的添加
#     pass
#
#
# p1 = person()
# p1.age = 10
# # p1.num=10 报错AttributeError: 'person' object has no attribute 'num'
# print(p1.age)

# class person:
# 	def shilifangfa(self):
# 	    print('实例方法',self)
#实例方法
# p=person()
# class Person:
#     def a(self):
#         print("实例方法",self)
# p=Person()
# p.a()
#类方法
# class person:
#     @classmethod
#     def leifangfa(cls):
#         print('类方法', cls)
#
# person.leifangfa()
#静态方法
# class person:
#     @staticmethod
#     def jingtaifanggfa():
#         print('静态方法')
#
# person.jingtaifanggfa()
# class Person:
# 		def shilifangfa(self,a):
# 			print("实例方法",self,a)
# p=Person()
# print(p)
# p.shilifangfa(12)

# class person:
#     def __func2(self):
#         print('这是一个私有类型的方法')
#     def a(self):
#         self.__func2()
#
# p=person()
# # p.a()
# class myclass:
# 	def __init__(self,realpart):
# 		self.r = realpart
#
# x=myclass(3.4)
# print(x.r)
# class person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#     def __str__(self):#信息格式化,用字符串描述实例,面向用户，通过print或str触发
#         return '姓名：{},年龄：{}'.format(self.name, self.age)
# p=person('sz',18)
# print(p)


# class person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#
#     def __str__(self):  # 信息格式化,用字符串描述实例,面向用户，通过print或str触发
#         return '姓名：{},年龄：{}'.format(self.name, self.age)
#
#
# p = person('sz', 18)
# print(p.name)
# print(p, type(p))  # 方法里的返回值#没有__str__方法时<__main__.person object at 0x04C86070>

# class person:
#     def __call__(self,age):
#         print(age)
# p = person()
# p(28)  # 使实例能被调用,传入参数
# p(23)
# p(14)


# class person:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, age):
#         print('姓名：{}，年龄：{}'.format(self.name, age))
#
#
# p = person('zyl')
# p(28)  # 使实例能被调用,传入参数
# p(23)
# p(14)
#
# class person:
#     def __init__(self):
#         self.cache = {}  # 增加一个字典属性
#
#     def __setitem__(self, key, value):  # 设置/增添键值
#         print('setitem', key, value)
#         self.cache[key] = value
#
#     def __getitem__(self, item):  # 获取键值
#         # print('getitem',item)
#         return self.cache[item]
#
#
#     def __delitem__(self, key):  # 删除操作
#          # print('setitem',key)
#         del self.cache[key]
#
#
# p = person()
# p['name'] = 'sz'  # setitem
# print(p['name'])  # getitem
# del p['name']
# print(p.cache)  # 查询字典


# class Person():
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         self.__age = value
#
#     age = property(get_age,set_age)
#
# p = Person()
# print(p.age)
# p.age = 98
# print(p.age)
# print(p.__dict__)

# class Person2(object):
#     def __init__(self):
#         self.__age = 18
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__age = value


# p2 = Person2()
# print(p2.age)
# p2.age = 98
# print(p2.age)
# print(p2.__dict__)

# class people:  # 类定义
#     name = ''  # 定义基本属性
#     age = 0  # 定义基本属性
#     __weight = 0  # 定义私有属性,私有属性在类外部无法直接进行访问
#
#     def __init__(self, n, a, w):  # 定义构造方法
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):  # 定义构造方法
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
# class student(people):  # 单继承示例,定义基类
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # super(student, self).__init__( n, a, w) # 调用父类的构函
            #super().__init__(name)  # 调用父类的一个方法，从父类获得继承
#         people.__init__(self, n, a, w)  # 调用父类的构函
#         self.grade = g
#
#     def speak(self):  # 覆写父类的方法
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
# p=people("tom", 3, 23)
# p.speak()
# test = student("Tim", 25, 80, 4)
# test.speak()

# class Animal():
#     def __init__(self, name):
#         self.name = name
#
#     def shengming(self):
#         print('dongwu')
#
#
# class Dog(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)  # 调用父类的一个方法，从父类获得继承
#
#         self.color = color  # 在子类中添加新的内容
#
#
#     def shengming(self):
#      print('gou')
#
#
#     def kanjia(self):
#      print('kanjia')
#
#
# a1 = Animal('a1')
# a2 = Dog('a2', 1)
# print(a1.shengming(), a2.shengming())

# import inspect
# class animal:
#     pass
# class person(animal):
#     pass
# inspect.getmro(person)  # 查看类资源的访问循序
# print(person.__mro__)
# print(person.mro())

# class D:
#     pass
#
# class B(D):
#     pass
#
# class C(D):
#     pass
#
# class A(C, B):
#     pass
#
# print(A.mro())

# class D(object):
#     def __init__(self):
#         print("enter----D")
#         print("leave----D")
#
# class B(D):
#     def __init__(self):
#         print("enter----B")
#         D.__init__(self)  # 调用父类的方法
#         print("leave----B")
#
# class C(D):
#     def __init__(self):
#         print("enter----C")
#         super().__init__()
#         print("leave----C")
#
# class A(C, B):
#     def __init__(self):
#         print("enter----A")
#         B.__init__(self)
#         C.__init__(self)
#         print("leave----A")
#
# a=A()
# print(a)
# print(A.__mro__)


# class D:
#     def __init__(self):
#         print("enter----D")
#         super().__init__()
#         print("leave----D")
#
# class B(D):
#     def __init__(self):
#         print("enter----B")
#         super().__init__()
#         print("leave----B")
#
# class C(D):
#     def __init__(self):
#         print("enter----C")
#         super().__init__()
#         print("leave----C")
#
# class A(C, B):
#     def __init__(self):
#         print("enter----A")
#         super(A, self).__init__()
#         # super().__init__()
#         print("leave----A")
#
# a=A()
# print(A.__mro__)

# class A(object):
#   def __init__(self):
#    print("enter A")
#    print("leave A")
#
# class B(object):
#   def __init__(self):
#    print("enter B")
#    print("leave B")
#
# class C(A):
#   def __init__(self):
#    print("enter C")
#    super(C, self).__init__()
#    print("leave C")
#
# class D(A):
#   def __init__(self):
#    print("enter D")
#    super(D, self).__init__()
#    print("leave D")
# class E(B, C):
#   def __init__(self):
#    print("enter E")
#    B.__init__(self)
#    C.__init__(self)
#    print("leave E")
#
# class F(E, D):
#   def __init__(self):
#    print("enter F")
#    E.__init__(self)
#    D.__init__(self)
#    print("leave F")
#
# f=F()
# print(F.__mro__)


#作业题1
# class A (object):
#     def run(self):
#         print("enter-----A")
# class B(object):
#     def run(self):
#         print("enter----B")
# class C(A,B):
#     def run(self):
#         print("entet-----C")
# c=C();
# c.run();
#作业题2
# class A(object):
#     def run(self):
#         print("enter----A")
# class B(object):
#     def run(self):
#         print("enter----B")
# class C(A):
#     pass
# class D(B):
#     pass
# class E(C,D):
#     pass
# e=E();
# e.run();
#作业题3
# class A(object):
#     pass;
#
#
# class B(object):
#     pass;
#
#
# class C(A):
#     def run(self):
#         print("C")
#
#
# class D(A):
#     def run(self):
#         print("D")
#
#
# class E(B, C):
#     def run(self):
#         super().run();
#
# #
# class F(E, D):
#     pass;
#
#
# f = F();
# print(F.__mro__)
# f.run()

# class F1:
#     def f1(self):
#         print("basketball")
#
# class Person(F1):
#     def f1(self):
#         print("Kobe")
#
# class Student(F1):
#     def f1(self):
#         print("Calvin")
#
# def func(arg):
#     return arg.f1()
#
# obj1=F1()
# obj2=Person()
# obj3=Student()
# func(obj1)
# func(obj2)
# func(obj3)

# from functools import singledispatch
#
# @singledispatch
# def function(obj):
#     print('%r' % (obj))
#
# @function.register(int)
# def function_int(obj):
#     print('Integer: %d' % (obj))
#
# @function.register(str)
# def function_int(obj):
#     print('String: %s' % (obj))
#
# @function.register(list)
# def function_list(obj):
#     print('List: %r' % (obj))
#
# if __name__ == "__main__":
#     function(1)
#     function('hello')
#     function(range(3))
#     function(object)

# import abc           #利用abc模块实现抽象类
# class animal(object, metaclass=abc.ABCMeta):
#     '''
#     这是抽象类
#     '''
#     @abc.abstractmethod     #定义抽象方法，无需实现功能
#     def jiao(self):
#         '''
#         抽象类的方法，子类必须调用，不调用报错
#         :return:
#         '''
#         pass
#
# class dog(animal):
#     def jiao(self):
#         '''
#         这是dog方法
#         :return: 无返回值
#         '''
#         print('wang')
#
# class cat(animal):
#     def jiao(self):
#         '''
#         这是cat方法
#         :return: 无返回值
#         '''
#         print('miao')
#
# def test(obj):
#     obj.jiao()
#
# c = cat()
# test(c)
# # c.jiao()

# class Dog(object):
#
#    def __init__(self,name):
#        self.name = name
#
#    @property
#    def eat(self):
#        print(" %s is eating" %self.name)
#
# d = Dog("ChenRonghua")
# d.eat

# class A(object):
#    def __init__(self):
#        print('A')
#        super(A, self).__init__()
#
# class B(object):
#    def __init__(self):
#        print('B')
#        super(B, self).__init__()
#
# class C(A):
#    def __init__(self):
#        print('C')
#        super(C, self).__init__()
#
# class D(A):
#    def __init__(self):
#        print('D')
#        super(D, self).__init__()
#
# class E(B, C):
#    def __init__(self):
#        print('E')
#        super(E, self).__init__()
#
# class F(C, B, D):
#    def __init__(self):
#        print('F')
#        super(F, self).__init__()
#
# class G(D, B):
#    def __init__(self):
#        print('G')
#        super(G, self).__init__()
#
# g = G()
# f = F()
# print(G.__mro__)
# print(F.__mro__)

# class F1:
#     def f1(self):
#         print("basketball")
#
# class Person(F1):
#     def f1(self):
#         print("Kobe")
#
# class Student(F1):
#     def f1(self):
#         print("Calvin")
#
# def func(arg):
#     return arg.f1()
#
# #在函数func中，如果我们接收一个变量 arg，则无论arg是F1,Person还是Student，都可以正确打印出结果：
# obj1=F1()
# obj2=Person()
# obj3=Student()
# func(obj1)
# func(obj2)
# func(obj3)

# from functools import singledispatch
# @singledispatch
# def a(num):
#     print(num)
# @a.register(int)
# def a(num1,num2):
#     print(num1,num2)
#
# # a(2)
# a(2,1)






