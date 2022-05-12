"""
=========================
File Name:python_basic11
Author:冯鑫
Date:2021/11/18-19:03
==========================
"""
'''
可变类型和不可变类型的区别
可变类型：数据的内容是可以更改，比如：列表、字典、集合
不可变类型：数据的内容不可更改，比如：数字、字符串、元组

有序：字符串、列表、元组
无序：字典、集合、数字
'''

# 1、区分重新赋值和更改内容

# 重新赋值
a = 100
a = 200  # 重新赋值
b = (1, 2, 3)
b = (1, 2, 3, 4)  # 重新赋值

# 修改数据内容
names = ['xiaohua', 'xiaolan', 'xiaobai']
print(id(names))  # 2572824633928
names[1] = 'xiaohong'  # 对列表的1号下标位置进行了修改，修改后地址不变
print(id(names))  # 2236156109384

# 2、不可变类型，不能修改内容
nums = (1, 2, 3, 4, 5)
# nums[1]=10 #元组不可变类型，不能修改内容
# print(nums)#TypeError: 'tuple' object does not support item assignment

'''

python 赋值、浅拷贝和深拷贝的区别
浅拷贝的使用方法： B = A.copy()
使用浅拷贝：当原容器对象中可变对象中有元素发生变化，拷贝的对象也会发生变化

深拷贝的使用方法： C = deepcopy(A)    
使用深拷贝：当原容器对象中可变对象中有元素发生变化，拷贝的对象不会发生变化

赋值操作：赋值会让新的变量也指向原容器的同一对象，赋值变量和原容器实际上是同一对象，所以任意一边更改，都会同时发生变化
 
'''
from copy import copy, deepcopy

list1 = [1, 2, [11, 22, 33], 'xiaohua', 'xiaobai']
list2 = list1  # 赋值
list3 = list1.copy()  # 浅拷贝
list4 = deepcopy(list1)  # 深拷贝

print('********************', '各列表数据', '*******************')
print(list1)  # [1, 2, [11, 22, 33], 'xiaohua', 'xiaobai']
print(list2)  # [1, 2, [11, 22, 33], 'xiaohua', 'xiaobai']
print(list3)  # [1, 2, [11, 22, 33], 'xiaohua', 'xiaobai']
print(list4)  # [1, 2, [11, 22, 33], 'xiaohua', 'xiaobai']

print('********************', '各列表地址', '*******************')
print(id(list1))  # 2476556258952
print(id(list2))  # 2476556258952
print(id(list3))  # 2476556877704
print(id(list4))  # 2476556877576

print('********************', '各列表可变元素对应的地址', '*******************')
print(id(list1[2]))  # 1897941255240
print(id(list2[2]))  # 1897941255240
print(id(list3[2]))  # 1897941255240
print(id(list4[2]))  # 1897941255240

print('********************', '更改原列表list1的可变元素后各列表中的数据', '*******************')
list1[2][0] = 666
print(list1)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai'] 原列表
print(list2)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai']  赋值表发生变化
print(list3)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai']  浅拷贝表发生变化
print(list4)  # [1, 2, [11, 22, 33], 'xiaohua', 'xiaobai']  深拷贝表没有任何变化

print('********************', '更改原列表list4的可变元素后各列表中的数据', '******************')
list4[2][0] = 888
print(list1)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai']
print(list2)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai']
print(list3)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai']
print(list4)  # [1, 2, [888, 22, 33], 'xiaohua', 'xiaobai']  只有深拷贝表发生变化

print('********************', '更改原列表list1的可变元素后各列表中的数据', '******************')
list1[0]=777
print(list1)  # [777, 2, [666, 22, 33], 'xiaohua', 'xiaobai']
print(list2)  # [777, 2, [666, 22, 33], 'xiaohua', 'xiaobai'] 赋值的表发生变化
print(list3)  # [1, 2, [666, 22, 33], 'xiaohua', 'xiaobai'] 浅拷贝未发生变化
print(list4)  # [1, 2, [888, 22, 33], 'xiaohua', 'xiaobai'] 深拷贝未发生变化


