# 1.面向对象三大特性，各有什么用处，说说你的理解
# 	    封装：将相同的属性和方法封装到一个函数里，使用时调用函数，减少代码量
#       继承：将共有的属性和方法写到父类里，子类里只写特有的属性和方法，减少代码量，增加扩展性
#       多态：对象行为和属性的多态
# 2.类的属性和对象的属性有什么区别?
# 		类属性定义在类内函数外 通过类访问,实例也能访问类属性 能被各个实例共享
# 		对象属性定义在类内函数内    通过实例访问，类不能访问实例属性    只作用于当前类
# 3. 面向过程编程与面向对象编程的区别与应用场景?
# 面向过程编程是一种以过程为中心的编程思想,分析出解决问题的步骤，然后用函数把这些步骤一步一步实现。面向过程编程，数据和对数据的操作是分离的。
# 面向对象编程是将事物对象化，通过对象通信来解决问题。面向对象编程，数据和对数据的操作是绑定在一起的。
# 4. 如下示例, 请用面向对象的形式优化以下代码
# def exc1(host,port,db,charset):
#        conn=connect(host,port,db,charset)
#        conn.execute(sql)
#        return xxx
#    def exc2(host,port,db,charset,proc_name)
#        conn=connect(host,port,db,charset)
#        conn.call_proc(sql)
#        return xxx
#    # 每次调用都需要重复传入一堆参数
#    exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
#    exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
#
# class Base(object):
#     host = "127.0.0.1"
#     port = 3306
#     db = "db1"
#     charset = "utf8"
#     def __init__(self,sql):
#         self.sql = sql
#         #根据传过来的sql语句判断执行哪个函数
#     def con(self):
#         return  "这是查询函数"
#     def conn(self):
#         return "这是储过程函数"
#
# base=Base("这是存储过程函数")
# print(base.con())
# print(base.conn())
#
# 5. 示例1, 现有如下代码， 会输出什么：
# class People(object):
#       __name = "luffy"
#       __age = 18
#
#   p1 = People()
# print(p1.__name, p1.__age)
# 报错，找不到__name和__age属性,__name和__age都是私有属性
# 6. 请执行以下代码，解释错误原因，并修正错误。
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
# d.eat()
# @property把eat（）变成了一个eat属性
# 把d.eat()改为d.eat
#
# 7. 多重继承的执行顺序，请解答以下输出结果是什么？
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
# g：GDAB
# f:FCBDA
# 8.请编写一段符合多态特性的代码.
# class F:
#     def f1(self):
#         print("这是基类")
#
# class Person(F):
#     def f1(self):
#         print("这是Person类")
#
# class Student(F):
#     def f1(self):
#         print("这是Student类")
#
# def func(arg):
#     return arg.f1()
#
# obj1=F()
# obj2=Person()
# obj3=Student()
# func(obj1)
# func(obj2)
# func(obj3)
# 9. 请写一个小游戏，人狗大站，2个角色，人和狗，游戏开始后，生成2个人，3条狗，互相混战，人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，人和狗具备的攻击力是不一样的
# 初始化人和狗的时候都需要给名字赋值；人个狗的血值都有默认值是100；各自的攻击力：人的攻击力是5，狗的攻击力是10
# class Animal(object):
#     def __init__(self,name):
#         self.name=name
#         self.blood=100
# class Person(Animal):
#     def __init__(self,name):
#         super(Person, self).__init__(name)
#         self.ATK=5
#     def battle(self):
#         if self.blood>10:
#             self.blood -= 10
#             print(self.name + "血量还剩" + str(self.blood))
#         else:
#             print("血量为0，你死了")
# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.ATK = 10
#     def battle(self):
#         if self.blood>5:
#             self.blood -= 5
#             print(self.name + "血量还剩" + str(self.blood))
#         else:
#             print("血量为0，你死了")
# p1=Person("zhangsan")
# p1.battle()
# p2=Person("lisi")
# p2.battle()
# p2.battle()
# d1=Dog("狗1")
# d1.battle()
# d2=Dog("狗2")
# d2.battle()
# d2.battle()
# d3=Dog("狗3")
# d3.battle()
# d3.battle()
# d3.battle()
#
# 10.编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.
# class Student(object):
#     num = 0
#     def __init__(self):
#         self.count()
#     # @staticmethod
#     # def count():
#     #     Student.num+=1
#     #     print(Student.num)
#     # @classmethod
#     # def count(cls):
#     #     Student.num+=1
#     #     print(Student.num)
#
# p=Student()
# m=Student()
# a=Student()
#
# 11.定义一个汽车类（Car），属性有颜色，品牌，车牌号，价格，
# 并实例化两个对象，通过初始化函数给属性赋值，并通过一个方法把所有属性输出
# class Car(object):
#     def __init__(self,color,brand,carNum,price):
#         self.color=color
#         self.brand = brand
#         self.carNum = carNum
#         self.price = price
#     def __str__(self):
#         return ("当前颜色为%s,品牌为%s,车牌号为%s,价格为%s"%(self.color,self.brand,self.carNum,self.price))
# a=Car("黑色","奥迪","382373","38383")
# print(a)
# 12.定义一个球员类(Player)，属性有身高，体重，姓名，实例化两个球员，分别是姚明和科比；通过初始化函数给属性赋值
# class Player(object):
#     def __init__(self,height,weight,name):
#         self.height=height
#         self.weight = weight
#         self.name = name
# yaoMing=Player(202,150,"姚明")
# kebe=Player(211,120,"科比")
#
# 13.设计一个立方体类Box，定义三个属性，分别是长，宽，高。定义二个方法，分别计算并输出立方体的体积和表面积。
# class Box(object):
#     def __init__(self,length,width,height):
#         self.length=length
#         self.width = width
#         self.height = height
#     def volume(self):
#         '''
#         这是计算体积的函数
#         :return:体积
#         '''
#         V=self.length*self.width*self.height
#         return V
#     def area(self):
#         '''
#         这是计算表面积函数
#         :return:表面积
#         '''
#         S=(self.length*self.width+self.length*self.height+self.width*self.height)
#         return S
# b=Box(20,30,40)
# print("体积为----"+str(b.volume()))
# print("表面积为----"+str(b.area()))
# 14.请定义一个交通工具(Vehicle)的类，其中有:
# 属性：速度(speed)，体积(size)等等
# 方法：移动(move(s))，设置速度(setSpeed(speed))，
# 加速speedUp(),减速speedDown()等等.
# 最后实例化一个交通工具对象，并初始化speed,size的值，
# 另外，调用加速，减速的方法对速度进行改变。
# 调用 move方法输出移动距离
# class Vehicle(object):
#     def __init__(self,speed,size):
#         self.speed=speed
#         self.size = size
#         # self.s=s
#     def move(self,s):
#         print("移动的距离为----"+str(self.speed*s))
#     def setSpeed(self,speed):
#         '''
#         根据传过来的参数决定是加速还是减速，如果传过来的是0，则减速，如果传过来的是1则加速
#         :param speed:
#         :return:
#         '''
#         if speed==1:
#            self.__speedUp()
#         elif speed==0:
#            self.__speedDown()
#     def __speedUp(self):
#          self.speed+=20
#          print(self.speed)
#     def __speedDown(self):
#          self.speed-=20
#          print(self.speed)
# V=Vehicle(200,300)
# V.move(2)
# V.setSpeed(1)
# V.move(2)
# 15.定义一个Hero类
# 属性有 power,name，分别代表体力值和英雄的名子，体力值默认为100；初始化中给名字赋值，体力默认100
# 方法有
# 1.) go() //行走的方法，如果体力值为0，则输出不能行走，此英雄已死亡的信息
# 2.) eat(int n); //吃的方法，参数是补充的血量，将 n的值加到属性power中，power的值最大为100，
# 3.) hurt();//每受到一次伤害，体力值－10，体力值最小不能小于0
# class Hero(object):
#     def __init__(self,name):
#         self.name=name
#         self.power=100
#     def go(self):
#         if self.power==0:
#             print("不能行走，此英雄已死亡")
#         else:
#             print("这是走的方法")
#     def eat(self,n):
#         if self.power+n<100:
#             self.power+=n
#             print(self.power)
#     def hurt(self):
#         if(self.power>10):
#             self.power -= 10
#             print(self.power)
#
# h=Hero("zhangsan")
# h.hurt()
# h.go()
# h.eat(2)
# 16.定义一个名为Vehicles（交通工具）的基类，该类中应包含str类型的成员属性brand（商标）和
# color（颜色），还应包含成员方法run（行驶，在控制台显示“我已经开动了”）和
# showInfo（显示信息，在控制台显示商标和颜色），并编写构造方法初始化其成员属性。
# 编写Car（小汽车）类继承于Vehicles类，增加int型成员属性seats（座位），
# 还应增加成员方法showCar（在控制台显示小汽车的信息），并编写构造方法。
# 编写Truck（卡车）类继承于Vehicles类，增加float型成员属性load（载重），
# 还应增加成员方法showTruck（在控制台显示卡车的信息），并编写构造方法。
# 以上子类在实例化时，都需要通过构造方法给属性赋值，在各自显示各自信息的方法中都需要先显示商标和颜色
# 在测试方法中测试以上各类。
# class Vehicles(object):
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color = color
#     def run(self):
#         print("我已经开动了")
#     def showInfo(self):
#         print("此交通工具的上商标为"+self.brand+"颜色为"+self.color)
# class Car(Vehicles):
#     def __init__(self,seats,brand,color):
#         super().__init__(brand,color)
#         self.seats=seats
#     def showCar(self):
#         self.showInfo()
#         print("座位数为"+str(self.seats))
# class Truck(Vehicles):
#     def __init__(self,load,brand,color):
#         super().__init__(brand,color)
#         self.load=load
#     def showTruck(self):
#         self.showInfo()
#         print("载重为"+str(self.load))
# l=Truck(6.3,"BYD","黑色")
# l.showTruck()
# c=Car(5,"BYD","黑色")
# c.showCar()
# v=Vehicles("BYD","黑色")
# v.run()
# v.showInfo()
# 17.建立三个类：居民、成人、官员。居民包含身份证号、姓名、出生日期，而成人继承自居民，
# 多包含学历、职业两项数据；官员则继承自成人，多包含党派、职务两项数据。
# 以上属性均为私有的实例属性
# 实例化成人和官员的对象，初始化函数中给属性赋值
# 为姓名创建get/set方法来操作姓名
# class Inhabitant(object):
#     def __init__(self,IDcard,name,brith):
#         self.__IDcard=IDcard
#         self.__name = name
#         self.__brith = brith
#     def setName(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
#     name=property(getName,setName)
# class adult(Inhabitant):
#     def __init__(self,IDcard,name,brith,education,job):
#         super().__init__(IDcard,name,brith)
#         self.__education = education
#         self.__job = job
# class officer(adult):
#     def __init__(self,IDcard,name,brith,education,job,position,party):
#         super().__init__(IDcard,name,brith,education,job)
#         self.__position = position
#         self.__party = party
#
# a=adult(292929,"zhangsan","19990101","大学","律师")
# print(a.name)
# a=officer(292929,"zhangsan","19990101","大学","律师","检察官","共产党")
# a.name="lisi"
# print(a.name)
#
# 18.编写出一个通用的人员类（Person），该类具有姓名（Name）、年龄（Age）、性别（Sex）。
# 然后对Person 类的继承得到一个学生类（Student），该类能够存放学生的多门课的成绩，
# 并能求出平均成绩。
# 以上属性均为私有的实例属性，通过初始化函数来为它们赋值；
# 需要创建对于的get/set方法来操作所有的私有的实例属性；
# 学生类中创建一个计算多门课程成绩的方法
# class Person(object):
#     def __init__(self,Name,Age,Sex):
#         self.__Name=Name
#         self.__Age = Age
#         self.__Sex = Sex
#
#     def setName(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
#     name = property(getName, setName)
#
#     def setAge(self,Age):
#         self.__Age = Age
#     def getAge(self):
#         return self.__Age
#     Age = property(getAge, setAge)
#
#     def setSex(self,Sex):
#         self.__Sex = Sex
#     def getSex(self):
#         return self.__Sex
#     Sex = property(getSex, setSex)
# class Student(Person):
#     def __init__(self,Name,Age,Sex,**kwargs):
#         super().__init__(Name,Age,Sex)
#         self.__sore=kwargs
#     def avgScore(self):
#         print(self.__sore)
#         self.avg=(sum(self.__sore.values())/len(self.__sore.values()))
#         print("平均成绩为",round(self.avg,2))
# s=Student("zhangsan",20,"女",English=20,math=30,physics =50)
# s.avgScore()
# s.name="lisi"
# print(s.name)
# s.age=21
# print(s.age)
# s.sex="男"
#
