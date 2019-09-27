import pymysql
class db(object):
    conn=None
    cursor = None
    def __init__(self):
        print("这是初始化函数")
    @classmethod
    def select(cls, sql, type, data):      #“查”函数
        db.link()
        try:
            if type[0]==0:     #此时返回一条结果
                cls.cursor.execute(sql,data)
                getDataFromDB=cls.cursor.fetchone()
                db.commit()
                return getDataFromDB
            if type[0] == 1:       #此时返回所有结果
                cls.cursor.execute(sql, data)
                getDataFromDB = cls.cursor.fetchall()
                db.commit()
                return getDataFromDB
            if type[0] == 2:           # 此时返回指定条数的结果
                cls.cursor.execute(sql, data)
                getDataFromDB = cls.cursor.fetchmany(type[1])
                db.commit()
                return getDataFromDB
            if type[0] ==3:        # 此时返回查询结果的条数
                cls.cursor.execute(sql, data)
                getDataFromDB = cls.cursor.rowcount()
                db.commit()
                return getDataFromDB
        except Exception as e:
            return "error"
    @classmethod
    def query(cls,sql,type,data):       #增加，修改，删除
        db.link()
        try:
            if type[0] == 0:        #增加一条，修改，删除
                print("这是执行增加函数")
                cls.cursor.execute(sql, data)
            if type[0] == 1:        #增加多条
                cls.cursor.executemany(sql, data)
            db.commit()
        except Exception as e:
            return "error"
    @classmethod
    def link(cls):      #连接数据库，获取游标
        if cls.conn == None:
            cls.conn = pymysql.Connect(
                host='localhost',  ##mysql服务器地址
                port=3306,  ##mysql服务器端口号
                user='root',  ##用户名
                passwd='zhao9988!',  ##密码
                db='djangomysql',  ##数据库名
                charset='utf8'  ##连接编码
            )
            cls.cursor = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)

    @classmethod
    def getLastId(cls):         #关闭游标和数据库
        return  cls.cursor.lastrowid
    @classmethod
    def close(cls):         #关闭游标和数据库
        cls.cursor.close()
        cls.conn.close()
    @classmethod
    def commit(cls):
        cls.conn.commit()
    def __close__(self):       #析构函数
        db.conn.close()