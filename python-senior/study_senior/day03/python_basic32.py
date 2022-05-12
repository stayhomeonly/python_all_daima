"""
# @Time : 2022/5/2 11:35
# @File : python_basic32
# @Project : python_0406
# @Content :
"""
"""
本章讲解:元组：tuple
元组的定义：元组和列表一样存储一组数据，但是元组为不可变类型，创建后不能修改数据
元组也是属于序列之一，有下标
"""

# 1、元组的声明,一般使用()
tup1 = ()  # 创建一个空元组
tup2 = (1, 2, 3, 'aaa', 'bbb', '哈哈哈')
print(tup2)

# 特别的声明方式
tup3 = (1,)  # 如果元组只保存一个数据，那么必须加 , 号
tup4 = (1)  # 如果不加，注意这个不是元组，是int类型
print(type(tup3))  # <class 'tuple'>
print(type(tup4))  # <class 'int'>

# 2.查看元组中的数据，通过下标访问
tup5 = (1, 2, 3, 'aaa', 'bbb', '哈哈哈')
print('元组tup5的2号位置是', tup5[2])  # 元组tup5的2号位置是 3
print('元组tup5的4号位置是', tup5[4])  # 元组tup5的4号位置是 bbb

# 3、元组为不可变类型，所以不能修改和删除
#  tup5[1] = 222   无法通过下标直接修改，会报错TypeError
#  print(tup5)
