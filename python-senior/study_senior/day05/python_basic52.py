"""
==================================
文件名: python_basic52
作者:    星光梁朝伟
时间:   2022/5/15-11:08
==================================
"""
"""
用for循环 遍历可迭代元素
语法 ： for 变量名 in 可以迭代元素(str list tuple dict set)
"""
# 遍历  就是把对象中的每个元素都拿出来过一遍
# 遍历字符串  2种方式  直接遍历  通过下标去遍历
str1 = '你的笑容很温暖'
# for a in str1:
#     print(a)
# for i in range(len(str1)):  # range(7) 0123456
#     print(str1[i])
# 遍历列表
list1 = [1, 2, 2, 3, 34, 555, 5]
# for a in list1:
#     print(a,end='  ')

# for i in range(len(list1)):
#     print(list1[i], end=' ')

# 遍历字典 重点********
dict1 = {1: 'xiaohua1', 2: 'xiaohua', 3: 'xiaohua', 4: 'xiaohua'}
# for i in dict1:  # 字典默认是操作键
#     print(i)
# for i in dict1.keys():  # 与上面的写法效果是一样的
#     print(i)
# for i in dict1.values():  # 遍历字典的值
#     print(i)
for a in dict1.items():  # 遍历字典所有的键值对
    print(a, type(a))
# 统计字典dict1的值中 xiaohua出现的次数
# cout1 = 0
# for i in dict1.values():
#     if i == 'xiaohua':
#         cout1 += 1
# print(cout1)
# 实例2 用for循环统计元组中某个元素出现的次数
# tup1 = (1, 2, 3, 5, 4, 85, 85, 41, 6, 5, 6, 87, 1, 2, 3, 15, 3)
# print(tup1.count(1))
# count2 = 0
# for b in tup1:
#     if b == 1:
#         count2 += 1
# print(count2)
# print(sorted(dict1))
a = 12345.9
b = str(a)
print(b)
for i in b:
    print(i)