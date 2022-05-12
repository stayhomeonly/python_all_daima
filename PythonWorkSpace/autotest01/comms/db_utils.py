"""
=========================
File Name:  db_utils01
Author:     Lee
Date:       2021/12/1-14:05
==========================
"""

import pymysql

from configparser import ConfigParser


class DBUtils(object):
    count = -1

    # 封装连接对象和游标对象
    def __init__(self):
        try:
            cf = ConfigParser()
            cf.read(filenames=r'D:\PythonWorkSpace\autotest01\conf\config.ini', encoding='utf-8')
            host = cf.get('mysql', 'host')
            port = cf.getint('mysql', 'port')
            user = cf.get('mysql', 'user')
            pwd = cf.get('mysql', 'password')
            db = cf.get('mysql', 'db')

            self.conn = pymysql.connect(host=host, port=port, user=user, passwd=pwd, db=db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('工具类连接出现异常,请检查DBUtils中的__init__方法!')
            print(e)

    # 封装关闭游标和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 封装查询结果及有多少条数据:条目数
    # 如果execute()括号里只传一个参数,我们需要运行 count = cursor.execute(sql)
    # 如果execute()括号传2个参数,我们需要运行 count = cursor.execute(sql,params)
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
            print('查询数据库条目数失败!', e)

    # 封装增删改
    # 如果execute()括号里只传一个参数,我们需要运行 count = cursor.execute(sql)
    # 如果execute()括号传2个参数,我们需要运行 count = cursor.execute(sql,params)
    def cud(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            if isinstance(params, tuple):
                self.count = self.cursor.execute(sql, params)
            if isinstance(params, list):
                self.count = self.cursor.executemany(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print('增删改执行失败!', e)

    # 封装查询一条数据:cursor.execute(sql),cursor.execute(sql,params)
    def find_one(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)  # 执行sql语句,并且把结果存在cursor里
                return self.cursor.fetchone()
            elif params is not None:
                self.cursor.execute(sql, params)
                return self.cursor.fetchone()
        except Exception as e:
            print('查询单条数据失败!', e)

    # 封装查询所有数据
    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)  # 执行sql语句,并且把结果存在cursor里
                return self.cursor.fetchall()
            elif params is not None:
                self.cursor.execute(sql, params)
                return self.cursor.fetchall()
        except Exception as e:
            print('查询所有数据失败!', e)


