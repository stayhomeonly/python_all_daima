"""
=========================
File Name:homework
Author:pengyumei
Date:2021/12/1-17:43
==========================
"""
'''
# 使用pymysql完成这些题目
1、使用python语言操作(查询) test库中的emp表
2、通过占位符方式查询出smith所在的部门名称,并且打印在控制台
3、通过占位符的方式查询出20部门的所有员工的信息。
4、通过占位符的方式查询出job为 SALESMAN的工资总和
5、查询出部门编号20有多少人？
6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
8、删除部门编号为 50的部门
'''
import pymysql
from day11.db_utils03 import DBUtils

# class DBUtils(object):
#     # 封装连接对象
#     def __init__(self):
#         try:
#             self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test')
#             self.cursor = self.conn.cursor()
#         except Exception as e:
#             print('工具类出现异常,请检查DBUtils中的__init__方法!')
#             print(e)
#
#     # 封装关闭游标和连接对象
#     def close(self):
#         self.cursor.close()
#         self.conn.close()
#
#     # 封装增删改
#     # 如果execute()括号里只传一个参数，我们需要运行count= cursor.execute(sql)
#     # 如果execute()括号里传2个参数，我们需要运行 count = cursor.execute(sql,params)
#     def cud(self, sql, params=None):
#         try:
#             if params is None:
#                 self.count = self.cursor.execute(sql)
#             if isinstance(params, tuple):
#                 self.count = self.cursor.execute(sql, params)
#             if isinstance(params, list):
#                 self.count = self.cursor.executemany(sql, params)
#             self.conn.commit()
#             return self.count
#         except Exception as e:
#             print('增删改执行失败', e)
#
#     # 封装查询一条数据
#     def find_one(self, sql, params=None):
#         try:
#             if params is None:
#                 self.cursor.execute(sql)  # 执行sql语句，并且把结果存在cursor里面
#                 return self.cursor.fetchone()
#             elif params is not None:
#                 self.cursor.execute(sql, params)
#                 return self.cursor.fetchone()
#         except Exception as e:
#             print('查询单条数据失败!', e)
#
#     #  封装查询所有数据
#     def find_all(self, sql, params=None):
#         try:
#             if params is None:
#                 self.cursor.execute(sql)  # 执行sql语句，并且把结果存在cursor里
#                 return self.cursor.fetchall()
#             elif params is not None:
#                 self.cursor.execute(sql, params)
#                 return self.cursor.fetchall()
#         except Exception as e:
#             print('查询所有数据失败!', e)


db = DBUtils()
# 1、使用python语言操作(查询)test库中的emp表
find_all = db.find_all("select * from emp;")
print(find_all)
#  2、通过占位符方式查询出smith所在的部门名称,并且打印在控制台
find_one = db.find_one("select DNAME from emp,dept where emp.DEPTNO=dept.DEPTNO and ENAME= %s;", ('SMITH',))
print(find_one[0])
# 3、通过占位符的方式查询出20部门的所有员工的信息
find_all = db.find_all("select * from emp where DEPTNO=%s;", ('20',))
print(find_all)
# 4、通过占位符的方式查询出job为 SALESMAN的工资总和
find_one1 = db.find_one("select sum(sal) from emp where JOB=%s;", ('SALESMAN',))
print(find_one1[0])
# 5、查询出部门编号20有多少人？
find_one2 = db.find_one("select count(ENAME) from emp where DEPTNO=%s;", ('20',))
print(find_one2[0])
# 6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
cud1 = db.cud("insert into dept(DEPTNO,DNAME,LOC) VALUES(%s,%s,%s);", ('50', 'Test', '上海'))
print(cud1)
# 7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
cud2 = db.cud("update dept set DNAME = %s where DEPTNO = %s;", [('TestSoftW', '50'), ('SLS', '30')])
# 8、删除部门编号为 50的部门
cud3 = db.cud("delete  from dept where DEPTNO = %s;", ('50',))

db.close()
