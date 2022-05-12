"""
=========================
File Name:python_senior01
Author:pengyumei
Date:2021/11/30-16:07
==========================
"""

'''
知识点:python操作mysql数据库，查询（查询单条、查询多条/查询所有)
'''

# 第一步：导入三方模块，pymysql是一个第三方的模块（我们需要先进行安装），在导包，然后通过pymysql操作mysql数据库
import pymysql

# 第二步：获取链接对象(我们需要指定mysql服务器的ip地址，端口号，用户名，密码，指定的库名
# localhost 和 127.0.0.1 都是代表本机的ip 地址(工作环境不会使用本机，用远端的）
# mysql默认的端口号是3306  oracle默认的端口号是1521  http默认的端口号80
# db是database的缩写，database(数据库)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='businessdb')
print(conn)

# 第三步 ：获取一个游标对象
cursor = conn.cursor()  # 游标能够存储结果集

# 第四步:通过游标对象执行sql语句，把结果存在cursor里，并且返回条目数
count = cursor.execute('select * from businessdb.account;')
print(count)  # 获取条目数

# 第五步：获取查询结果

# 1、获取所有数据
data = cursor.fetchall()
print(data)  # 返回结果集中的所有数据，格式((元组1),(元组2))

# 2、获取结果集中的一行数据
data = cursor.fetchone()  # 返回一行数据，并且包装成元组
print(data)

# 3、获取结果集中的多种数据
data = cursor.fetchmany(2)  # 获取结果集的2行数据
print(data)  # 返回多条数据，格式：((元组1),(元组2),......)

# 3条不能同时执行，必须单独执行一个


# 第六步：关闭游标
cursor.close()

# 第七步：关闭连接
conn.close()
