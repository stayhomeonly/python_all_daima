"""
=========================
File Name:python_senior02
Author:pengyumei
Date:2021/12/1-10:16
==========================
"""

# 1.增加SQL代码可读性
# 2.占位符可以预先编译，提高执行效率
# 3.防止SQL注入
# 4用占位符的目的是绑定变量，这样可以减少数据SQL的硬解析，所以执行效率会提高不少
'''
知识点：python操作mysql数据库，通过占位符查询
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

# 第四步:把活的数据通过%s进行占位，在通过元组进行赋值[这种方式更加安全，他会先发送sql语句,在发送参数数据】
cursor.execute("select * from account where name = %s and age = %s;",('aa',20))# 防止sql注入

# 第五步：获取查询结果

# 1、获取所有数据
data = cursor.fetchall()
print(data)  # 返回结果集中的所有数据，格式((元组1),(元组2))






# 第六步：关闭游标
cursor.close()

# 第七步：关闭连接
conn.close()
