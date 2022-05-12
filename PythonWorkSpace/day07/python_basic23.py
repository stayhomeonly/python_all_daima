"""
=========================
File Name:python_basic23
Author:冯鑫
Date:2021/11/23-11:25
==========================
"""
# 知识点1：自动组包

num = 1, 2, 3
print(num)  # (1, 2, 3) 将多个元素组成一个元组

group = 10, 'tom', {'name': 'xiaohua', 'age': 18}
print(group)  # (10, 'tom', {'name': 'xiaohua', 'age': 18})
print(type(group))  # <class 'tuple'>

# 知识点2：自动拆包
list1 = ['xiaohua', 10, '1001']
name, age, id = list1
print(name, age, id)  # xiaohua 10 1001

tup1 = ('xiaohua', 10, '1001')
name, age, id = tup1
print(name, age, id)  # xiaohua 10 1001

dic1 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}
n, a, s = dic1
print(n, a, s)  # name age sex 字典拆包默认时key

# 在函数调用的过程中，如果在变量前加*号，代表拆包
print(*list1)  # xiaohua 10 1001
print(*tup1)  # xiaohua 10 1001
print(*dic1)  # name age sex

# 在拆包过程中，可以使用*将多个变量的值存在一个列表中，这里用*组包
names = ('小张', '小王', '小李', '小白', '小花', '哈哈')

name1, *name = names  # *name：将其余数据打包赋值给name
print(name1)  # 小张
print(name)  # ['小王', '小李', '小白', '小花', '哈哈']

name1, name2, *name = names
print(name1)  # 小张
print(name2)  # 小王
print(name)  # ['小李', '小白', '小花', '哈哈']

*name, name1 = names
print(name)  # ['小张', '小王', '小李', '小白', '小花']
print(name1)  # 哈哈

name1, *name, name2 = names
print(name1)  # 小张
print(name)  # ['小王', '小李', '小白', '小花']
print(name2)  # 哈哈

# *name1,*name2=names#SyntaxError: two starred expressions in assignment
# print(name1)
# print(name2)
