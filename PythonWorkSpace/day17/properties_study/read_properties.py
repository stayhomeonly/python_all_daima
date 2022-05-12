"""
=========================
File Name:read_properties
Author:冯鑫
Date:2021/12/8-11:16
==========================
"""
from configparser import ConfigParser

# 创建一个解析类的对象
cnp = ConfigParser()

# 读取文件
cnp.read(filenames=r'./config.ini', encoding='utf-8')
host = cnp.get('mysql', 'host')
print(host)  # 127.0.0.1

pwd = cnp.get('mysql','password')
print(pwd)  # 123456
print(type(pwd))  # <class 'str'>

# 注意get读取的默认都是字符串，我们也可以读取成其他类型

port = cnp.getint('mysql','port')
print(port)  # 3306
print(type(port))  # <class 'int'>


