def list1(request):
# 往数据库里存1000条数据
    i=0;
    data=[]
    while i<1000:
    # username的取值范围有：张三，李四，王五，小明，小宏
        userList=["张三","李四","王五","小明","小宏"]
        username=random.sample(userList,1)
        # print(username)
             # password的取值范围：1000 - 10000
        pwd=random.randint(1000,10000)
        # print(pwd)
        # email的值为a @ 163.com a的范围是a - z的随机4位
        word="".join(random.sample(string.ascii_lowercase, 4))
        email=word+"@163.com"
        # print(email)
        # registtime的值为前1000天，24小时随机，分钟随机秒随机
        now=datetime.now()
        registtime=now-timedelta(days=random.randint(0,1000),hours=random.randint(0,23),minutes=random.randint(0,59),seconds=random.randint(0,59))
        registerStrTime=datetime.strftime(registtime,"%Y-%m-%d %H:%M:%S")
        # print(registtime)
        tu=(username,pwd,email,registerStrTime)
        data.append(tu)
        i+=1

    sql = "insert into userinfo(userName,pwd,email,registertime)values(%s,%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

    # 获取渲染数据


    return render(request,'article/list1.html')