'''
---------------------------
File Name:Get_ChildNodeinfo
Author:FENGXIN
date:2022/2/28-21:19

---------------------------

'''
from xml.dom import minidom

# 打开文件
dom = minidom.parse("Class_info.xml")

# 加载文件
root = dom.documentElement

tags = root.getElementsByTagName("student")

print(tags[0].nodeName)
print(tags[0].nodeType)
print(tags[0].nodeValue)
