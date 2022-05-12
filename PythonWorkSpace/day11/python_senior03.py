"""
=========================
File Name:python_senior03
Author:pengyumei
Date:2021/12/1-11:43
==========================
"""

'''
知识点：python操作sql，进行增删改
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

# 第四步:通过游标对象执行sql语句
# count = cursor.execute("insert into account(name,age,nickname) values('xiaowang',30,'王小帅');")
# count = cursor.execute("insert into account(name,age,nickname) values(%s,%s,%s);", ('迟迟', 30, '小迟迟'))
# count = cursor.execute("update account set name = '迟迟mini'where name='迟迟plus MAX';")
# count = cursor.execute("update account set name = %s where name= %s;",('迟迟','迟迟mini'))
count = cursor.execute("delete from account where name = %s;", ('迟迟',))
print(count)  # 1
# 第五步：增删改都需要提交,不能忘记,否则数据库数据不变
conn.commit()

# 第六步：关闭游标
cursor.close()

# 第七步：关闭连接
conn.close()
