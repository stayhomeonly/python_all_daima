'''
---------------------------
File Name:Get_Nodelnfo
Author:FENGXIN
date:2022/2/26-21:48

---------------------------

'''
from xml.dom import minidom

# 打开xml文件
dom = minidom.parse("Class_info.xml")
# 获取文档对象元素
root = dom.documentElement

print(root.nodeName)  # nodeName 节点名称
print(root.nodeValue)  # nodeValue 返回文本节点的值
print(root.nodeType)  # 属性返回以数字值返回指定节点的节点类型
# 如果节点是元素节点，则nodeType属性将返回1
# 如果节点是属性节点，则nodeType属性将返回2
