"""
=========================
File Name:python_basic12
Author:xu
Date:2021/11/18-15:47
==========================
"""
"""
类型转换
"""
"""
知识点1、数字类型和布尔类型互相转
"""
# (1)除了0以外，所有整数转换为bool类型，值都是 True
# (2)除了0.0以外，所有浮点数转换为bool类型，值都是 True

# bool()函数：可以强制将数据转换为bool类型
# int()函数：可以将数据强制转换为整数类型
# float()函数：可以将数据强制转换为浮点数类型
# str()函数：可以将数据强制转换为字符串类型
# 注意：并不是一定能转换成功

# 1.1整数转换布尔类型

c = 1
bo3 = bool(c)  # 将整数类型的c转换为bool类型,转换之后将值给bo3
print(bo3)  # True

d = 0
bo4 = bool(d)
print(bo4)  # False

#  1.2浮点数转换布尔类型

e = 1.0
bo5 = bool(e)  # 将浮点数转换为bool类型
print(bo5)  # True

f = 0.0
bo6 = bool(f)
print(bo6)  # False

#  1.3布尔类型转换为浮点数或者整数

bo7 = True
bo8 = False
print(int(bo7), int(bo8))  # 当布尔类型转换为整数时，True和False分别转换为1和0，固定转换
print(float(bo7), float(bo8))  # 当布尔类型转换为浮点数时，True和False分别转换为1.0和0.0，固定转换

"""
总结：非0为真，非0为True
"""

"""
知识点2、整数和浮点数互相转换,当浮点数转换为整数的时候会导致精度丢失
"""
f = 3.55  # f是浮点数类型
i = int(f)  # 将浮点数类型的f强制转换为整数类型
print(i)  # 3

"""
知识点3、字符串和数字可以互相转换，但是字符串转数字必须保证被转的值是数字类型
"""

# 3.1 数字转字符串
age = 18
print(type(age))  # <class 'int'>
age = str(age)  # 将数字18转换为字符类型
print(type(age))  # <class 'str'>

# 3.2 字符串转化为数字（字符串转数字必须保证被转的值是数字类型）
name = 'xiaohua'
print(type(name))  # <class 'str'>
# name = int(name)  # 字符串'xiaohua'不是数值，无法转换为数字，ValueError: invalid literal for int() with base 10: 'xiaohua'

tel = '15865656565'
print(type(tel))  # <class 'str'>
tel = int(tel)  # 这个转换没有报错，因为tel里面装的是数值
print(type(tel))  # <class 'int'>

# 3.3字符串转换为布尔类型
name = 'xiaohua'
bo1 = bool(name)
print(bo1)  # True
name1 = ''  # 这是声明了一个字符串类型的空值
bo2 = bool(name1)
print(bo2)  # False

"""
数字转字符：可以直接转，基本不受限制
字符转数字：需要被转化的字符串必须是纯数值
数字转布尔：非0为True
布尔转数字：True为1，False为0
字符串转布尔：非空为True
"""

"""
知识点4、列表、元组、字典、集合转字符串
"""
list1 = ['a', 'b', 'c']
str1 = str(list1)
print(type(str1))  # <class 'str'>

dict1 = {'name': 'xiaohua', 'age': 18}
str2 = str(dict1)
print(str2, type(str2))

# 元组可转换
# 集合可转换
# 任意类型都可以转换为字符串

"""
知识点5：列表、集合和元组互相转换
"""
list1 = ['a', 'b', 'c']
print(tuple(list1))  # 列表转元组  ('a', 'b', 'c')
print(set(list1))  # 列表转集合,可以去重 {'b', 'a', 'c'}

tup1 = (1, 2, 3)
print(list(tup1))  # 元组转列表  [1, 2, 3]
print(set(tup1))  # 元组转集合,可以去重  {1, 2, 3}

set1 = {11, 22, 33}
print(list(set1))  # 集合转列表 [33, 11, 22]
print(tuple(set1))  # 集合转元组 (33, 11, 22)

"""
知识点6：将列表、元组、集合里面的元素拼接为字符串  .join(),使用.join()连接元素时，必须保证所有的元素都是字符类型
                                            如果被连接的对象里面有其它类型，会产生报错TypeError
"""
str3 = 'abcd'
str4 = '*'.join(str3)
print(str4)  # a*b*c*d

# 将列表、元组、集合的元素进行连接,

print('列表' * 100)
list2 = ['a', 'b', 'c']
str5 = '-'.join(list2)  # 将 '-' 加入到list2列表中，将列表的元素进行连接，转换为一个字符串类型
print(str5)  # a-b-c
str5 = ''.join(list2)  # 将 ''(空字符串) 加入到list2列表中，将列表的元素进行连接，转换为一个字符串类型
print(str5)  # abc

print('元组' * 100)
tup2 = ('a', 'b', 'c')
str5 = ''.join(tup2)
print(str5)  # abc

print('集合' * 100)
set2 = {'a', 'b', 'c'}
str5 = ''.join(set2)
print(str5)  # abc

# 创建空数据
str1 = str()  # 创建一个空字符串
print(str1)  # 打印空
print(1)
num1 = int()  # 创建一个整数，不赋值，默认为0
print(num1)  # 0

list1 = list()  # 创建空列表
print(list1)  # []

set1 = set()  # 创建空集合
print(set1)  # set()

tup1 = tuple()  # 创建一个空列表
print(tup1)  # ()
