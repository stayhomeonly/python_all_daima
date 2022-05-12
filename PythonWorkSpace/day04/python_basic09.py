"""
=========================
File Name:python_basic09
Author:冯鑫
Date:2021/11/18-10:27
==========================
"""
'''
本章讲解：set 集合
集合的定义：{value1,value2,value3,value4........}
集合的特点：无序，没有下标索引，集合里面的数据不能重复，可变类型
集合里面只能存放不可变类型的元素
'''

# 知识点1：集合的定义
set1 = {11, 22, 33, 44}
print(set1)  # {33, 11, 44, 22}

# set2={11,22,33,'a',(1,2,3),[1,2,3]}#因为里面有个可变类型：列表，所以产生报错，TypeError: unhashable type: 'list'

set3 = {11, 22, 33, 44, 11, 22}
print(set3)  # {33, 11, 44, 22} 自动过滤重复元素

# 知识点2：集合添加单个元素 .add()
set3 = {11, 22, 33, 44}
set3.add('abc')  # 给集合set3添加元素‘abc’
print(set3)  # {33, 11, 44, 22, 'abc'}

# 知识点3：集合添加个多个元素 .update()
set4 = {11, 22, 33, 44}
set4.update({'aaa', 'bbb', 'ccc', 11})  # 给set添加多个元素
print(set4)  # {33, 'ccc', 'bbb', 11, 44, 'aaa', 22}

# 知识点4：移除元素 .remove()
set5 = {33, 'ccc', 'bbb', 11, 44, 'aaa', 22}
set5.remove(11)  # 删除set5中的元素11
print(set5)  # {33, 'ccc', 'bbb', 44, 'aaa', 22}

# 知识点5：移除元素2：.discard()
set5 = {33, 'ccc', 'bbb', 11, 44, 'aaa', 22}
set5.discard('aaa')
print(set5)  # {33, 'bbb', 11, 'ccc', 44, 22}

# 知识点6：清空元素 .clear()
set6 = {33, 'ccc', 'bbb', 11, 44, 'aaa', 22}
set6.clear()  # 清除set6中的所有数据
print(set6)  # set()

# 彻底删除使用del
set6 = {33, 'ccc', 'bbb', 11, 44, 'aaa', 22}
del set6
# print(set6) 会报错：SyntaxError: invalid character in identifier

# 知识点7：交集 intersection 并集 union
set1= {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

set3 = set1.intersection(set2)  # 表示：set1和set2相交的集合
print(set3)#{4, 5, 6}

#还有一种写法
print(set1&set2) #{4, 5, 6},交集的另外一种写法

set4=set1.union(set2) #表示：set1和set2并集元素
print(set4)#{1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set1| set2)#{1, 2, 3, 4, 5, 6, 7, 8, 9},并集的另外一种写法

#获取差集
print(set1-set2) # 表明在set1中有，set2中是没有的

#知识点8：函数 len()/in/not in/max()/min()........
set1= {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print(len(set1))#6
print(max(set1))#6
print(min(set3))#4
print(sum(set1))#21
print(1 in set1)#True
print(1  not in set2)#True

# 集合没有下标
set1 = {1,2,3,4,5,6}
#print(set1[1])  # 集合没有下标，强行使用会报错：TypeError: 'set' object does not support indexing
