"""
=========================
File Name:db_utils02
Author:pengyumei
Date:2021/12/1-15:12
==========================
"""
import pymysql


class DBUtils(object):
    count = -1

    # 封装连接对象和游标对象
    def __init__(self):

        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('工具类出现异常,请检查DBUtils中的__init__方法!')
            print(e)

    # 封装关闭游标和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 封装查询结果及有多少条数据：条目数
    # 如果execute()括号里只传一个参数，我们需要运行count=cursor.execute(sql) sal是执行语句
    # 如果execute()括号传2个参数,我们需要运行 count=cursor.execute(sql,params)params是参数的意思

    def find_count(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
                return self.count
            if params is not None:
                self.count = self.cursor.execute(sql, params)
                return self.count
        except Exception as e:
            print('查询数据库条目数失败', e)

    # 封装增删改
    # 如果execute()括号里只传一个参数，我们需要运行count= cursor.execute(sql)
    # 如果execute()括号里传2个参数，我们需要运行 count = cursor.execute(sql,params)

    def cud(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print('增删改执行失败!', e)


if __name__ == '__main__':
    db = DBUtils()
    count = db.find_count('select * from account where name = %s;', ('aa',))
    print(count)  # 1

    cud = db.cud('delete from account where name = %s;', ('lisi',))
    print(cud)  # 1
    db.close()
