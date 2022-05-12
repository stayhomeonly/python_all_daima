'''
---------------------------
File Name:Get_NodeValue
Author:FENGXIN
date:2022/2/27-20:26

---------------------------

'''

from xml.dom import minidom

# 打开xml文件
dom = minidom.parse("Class_info.xml")
# 获取文档对象元素
root = dom.documentElement
# 根据标签名称获取标签对象
names = root.getElementsByTagName('name')
ages = root.getElementsByTagName('age')
citys = root.getElementsByTagName('city')

print(names[0].firstChild.data)
print(ages[0].firstChild.data)
print(citys[0].firstChild.data)

for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)




