"""
=========================
File Name:db_utils01
Author:pengyumei
Date:2021/12/1-14:43
==========================
"""
import pymysql


class DBUtils(object):
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


if __name__ == '__main__':
    db = DBUtils()
    print(db)
    db.close()
