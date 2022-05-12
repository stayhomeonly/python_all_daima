"""
=========================
File Name:db_untils04
Author:pengyumei
Date:2021/12/1-17:12
==========================
"""

from day11.db_utils03 import DBUtils

# 创建DBUtils 的实例对象，自动获取连接对象和游标对象
db = DBUtils()

cud = db.cud("insert into account(name,age,nickName) Values(%s,%s,%s);",('小马',35,'化腾'))
print(cud) #1 接收收到的条目数

find_all = db.find_all("select * from account;")
print(find_all)

db.close()
