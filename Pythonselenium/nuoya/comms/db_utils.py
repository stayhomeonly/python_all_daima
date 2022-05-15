"""
#@Time：2022/5/14-13:36
#@file：db_utils
#@Project:Pythonselenium
#@Content:

"""
import pymysql

from nuoya.comms.public import get_ini_data


class DBUtils(object):
    count = -1  # 因为条目数不可能是负数,所以初始值为-1,这样一旦返回-1就证明程序失败

    # 封装连接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=get_ini_data('mysql', 'host'),
                                        port=int(get_ini_data('mysql', 'port')),
                                        user=get_ini_data('mysql', 'user'),
                                        passwd=get_ini_data('mysql', 'password'),
                                        db=get_ini_data('mysql', 'db'))
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库工具类连接出现异常,请检查DButils中的__init__方法!")
            print(e)

    # 封装关闭游标对象和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

        # 封装查询结果集有多少条数据:条目数
        # 如果execute()括号里只传一个参数,我们需要运行: count = cursor.execute(sql)
        # 如果execute()括号里传2个参数,我们需要运行: count = cursor.execute(sql,占位符数据(元组))

    def find_count(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
                return self.count
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
                return self.count
        except Exception as e:
            print("查询数据库条目数失败!", e)

    # 封装查询一条数据: execute(sql)   execute(sql,params)
    def find_one(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)  # 执行sql语句并且把结果存在cursor
            elif params is not None:
                self.cursor.execute(sql, params)
            return self.cursor.fetchone()  # 从结果集获取一条数据
        except Exception as e:
            print("查询单条数据失败!", e)

    # 封装查询所有数据: execute(sql)   execute(sql,params)
    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)  # 执行sql语句并且把结果存在cursor
            elif params is not None:
                self.cursor.execute(sql, params)
            return self.cursor.fetchall()  # 从结果集获取所有数据
        except Exception as e:
            print("查询所有数据失败!", e)


if __name__ == '__main__':
    # db = DBUtils()
    # data = db.find_one("select * from nmp_business.t_scene where scene_code = %s;", ("jingxuan12345",))
    # # print(data)
    # # print(data[0], type(data[0]))
    # scoureID = str(get_id()) + str(data[0])
    # print(scoureID, type(scoureID))
    # db.close()
    db = DBUtils()
    data = db.find_count("select * from nmp_business.t_message_sms_record where id =%s;",('19101466758032439584503',))
    print(data)
