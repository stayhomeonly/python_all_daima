'''
---------------------------
File Name:Get_NodeAttribute
Author:FENGXIN
date:2022/2/27-21:01

---------------------------

'''
from xml.dom import minidom

# 打开文件
dom = minidom.parse("Class_info.xml")

# 获取文档对象元素
root = dom.documentElement

# 获取元素名称
logins = root.getElementsByTagName('login')


for i in range(2):
    username = logins[i].getAttribute("username")  # getAttribute 获取属性名称
    print(username)
    password=logins[i].getAttribute('password')
    print(password)