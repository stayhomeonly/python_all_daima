"""
=========================
File Name:python_baisic20
Author:冯鑫
Date:2021/11/22-15:58
==========================
"""
'''
for 循环迭代（遍历） str/list/tuple/dict/set
万物皆可for循环
'''
# 知识点1：遍历各类型
# 遍历列表
# list1=[1,2,3,4,5,6,7,8,9]
# for i in list1:# i in range(1,11)
#     print(i) #每一次循环，都将list1中的一个值给i，直到最后一个值结束
#
# #遍历元组
# tup1=(1,2,5,7,4,2,6)
# for i in tup1:
#     print(i)

# 遍历集合
# set1={1,2,3,4,'xiaohua','huahua',(1,2,3)}
# for i in set1:
#     print(i)

# 遍历字符串
# str1 = '今天好冷,秋裤穿了吗'
# for i in str1:
#     print(i, end='')

# 知识点2：打印时不换行
# print('a',end='-')
# print('b')
# print('c')

# 知识点3：range()函数补充
# for i in range(5):#如果range不写开始位置，默认开始位置就是0，这里的这个5是结束位置
#      print(i)

# 知识4：通过下标遍历，前提是被遍历的对象是序列
list2 = ['xiaohua', 'xiaobai', 'xiaohong', 'xiaomei']
# list[0]    list[1]   list[2]  list[3]

# for i in range(0,4)  :#版本1
#     print(list2[i])

# for i in range(0,len(list2)) :#版本2
#     print(list2[i])

# for i in range(len(list2)) :
#     print(list2[i],end=' ') #该列表长度4，i in range (4),那么i的值（0，1，2，3）

# tup2 = ('xiaohua', 'xiaobai', 'xiaohong', 'xiaomei', 'haha')
# for i in range(len(tup2)):
#     print(tup2[i])
str2 = '今天是小雪'
for i in range(len(str2)):
    print(str2[i], end='')
print()

'''
特别知识点：通过值遍历，遍历字典
'''
dict1 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}
# 回想知识点：
print(dict1.keys())  # dict_keys(['name', 'age', 'sex'])
print(dict1.values())  # dict_values(['xiaohua', 18, '女'])
print(dict1.items())  # dict_items([('name', 'xiaohua'), ('age', 18), ('sex', '女')])

for i in dict1.keys():  # 遍历字典的key
    print(i)
for i in dict1.values():
    print(i)
for i in dict1.items():
    print(i)
for i in dict1.keys():
    print(i, '对应的值是：', dict1.get(i))
# 练习：统计出（0，2，3，4，2，7，2，6，4）中2出现的次数

count1 = 0
list4 = [0, 2, 3, 4, 2, 7, 2, 6, 4]
for i in list4:
    if i == 2:
        count1 = count1 + 1
print(count1)

# 通过下标遍历
count2 = 0
for i in range(len(list4)):
    if list4[i] == 2:
        count2 += 1
print(count2)  # 3

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}'.format(i, j, i * j), end='   ')
    print()
