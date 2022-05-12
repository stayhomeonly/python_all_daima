"""
# @Time : 2022/5/2 14:35
# @File : python_basic34
# @Project : python_0406
# @Content :
"""
"""
可变类型：列表，集合，字典
不可变类型：数字，字符串，元组

有序：字符串、列表、元组
无序：数字、集合、字典

"""
# 查看物理地址 id(),地址随机分配，可能每次运行都不相同

# 区别一下重新赋值和修改
a = 100
a = 200  # 这是重新赋值

b = [1, 2, 3]
b[1] = 222  # 这是修改内容

tup1 = ("xiaohua", "xiaobai", "xiaowang")
print(id(tup1))  # 1755322471048
tup1 = ("xiaohua", "xiaohei", "xiaowang")  # 重新赋值
print(id(tup1))  # 1755322471336

# 可变类型，可以直接修改内容，比如列表
list1 = ["xiaohua", "xiaobai", "xiaowang"]
print(id(list1))  # 2168715764296  这个是更改前列表对应的物理地址
list1[1] = "xiaohei"
print(list1)  # ['xiaohua', 'xiaohei', 'xiaowang']
print(id(list1))  # 2168715764296  这个是更改后对应的物理地址，与更改前一致，说明都是同一对象

# 不可变类型，声明后不能修改内容，比如元组
tup1 = ("xiaohua", "xiaobai", "xiaowang")
# tup1[1] = "xiaohei"  # 无法修改


# 有序：字符串、列表、元组，有下标，可通过下标进行访问
stra = "abcdefg"
print(stra[0])  # a 可通过下标访问
lista = ['a', 'b', 'c']
print(lista[0])  # a 可通过下标访问
tupa = ('a', 'b', 'c')
print(tupa[0])  # a 可通过下标访问

# 无序：数字、集合、字典
inta = 12345
# print(inta[0])  # 无序的，没有下标的概念
seta = {'a', 'b', 'c'}
# print(seta[0])  # 无序的，没有下标的概念
