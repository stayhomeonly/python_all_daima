"""
=========================
File Name:python_basic18
Author:冯鑫
Date:2021/11/19-16:22
==========================
"""

'''
whlie循环

语法
while 条件:
    语句块
    
当条件成立时执行语句块，重复执行    
          
'''
import random

# # 循环案列1：打印1-100的整数
# i = 1
# while i <= 100:  # 每次执行完语句后，从本行重新开始，只要本行的条件时成立的，一直运行
#     print(i)
#     i += 1
#
# # 循环案列2：打印0-100的偶数
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# # 循环案列3：求出1-100所有数的和
# i = 1
# sum1 = 0
# while i <= 100:
#     sum1 = sum1 + i
#     i += 1
#     print(sum1)
#
# # 循环案列4：求出0-100有多少个偶数
# i = 0
# count1 = 0
# while i <= 100:
#     if i % 2 == 0:
#         count1 += 1
#     i += 1
# print(count1)
# # 求出0-30有少个奇数
# i = 0
# count1 = 0
# while i <= 30:
#     if i % 2 == 1:
#         count1 += 1
#     i += 1
# print(count1)
# 练习1：输入一个年份，判断是否为闰年（能被4整除且不能被100整除，或者能被400整除）
# date = int(input('请输入年份：'))
# if  (date % 4 == 0 and date % 100 != 0 ) or date % 400 == 0:
#     print('%d是闰年' % date)#print(str(date)+'%d是闰年' )另外一种写法
# else:
#     print('%d不是闰年' % date)


# 练习2：用户输入三个边，先判断是否构成三角形，再判断是否为等腰三角形（任意两边相加大于第三边，任意两边相减小于第三边）
# a = float(input('请输入边长1:'))
# b= float(input('请输入边长2:'))
# c= float(input('请输入边长3:'))
# if (a+b>c) and (a+c>b) and (a+c>b):
#     print('是三角形')
#     if a==b or b==c  or c==a:
#         print('这是一个等腰三角形')
#     else:
#         print('这是一个普通三角形')
# else:
#     print('不是三角形')

"""
练习3：猜大小
规则：1、有三个骰子，每个骰子大小从1-6点，用户可以输入押注金额和竞猜内容(大或者小)
      2、随机产生三个筛子的大小，并求出他们的和，和为3-10是小，和为11-18是大
      3、如果猜对了，打印获得双倍的奖金XXX元，如果猜错则输掉押注金额
      
"""

# import random
# d=input('请输入押注金额:')
# f=input('竞猜内容大或者小：')
# g=random.randint(1,6)
# e=random.randint(1,6)
# h=random.randint(1,6)
# print('三个骰子分别是:', g,e,h)
# if  3<=(g+e+h)<=10:
#     print('小')
#     if f=='小':
#         print(float(d)*2)
#     else:
#         print('输掉赌注')
# elif 11<=(g+e+h)<=18:
#     print('大')
#     if f=='大':
#         print(float(d)*2)
#     else:
#         print('输掉赌注')
# else:
#     print('输入错误')


"""
练习4：红球6个（1-33），蓝球1个（1-16）
# 1、创建一个空列表长度为7
# 2、循环随机数1-33的数字加入到列表中，且判断该列表中是否存在该数字，如果不存在则放入，如果存在则不放入，直到满6个数为止
# 3、生成篮球1-16随机，并且存在最后一位
# 4.附加要求：所有个位数字必须有0


"""
list1 = list()

while True:
    x = random.randint(1, 33)
    if x not in list1:
        list1.append(x)
        list1.sort()
    if len(list1) == 6:
        break

list1.append(random.randint(1, 16))
print(list1)

list2 = list(map(lambda x: str(x), list1))

for i in range(len(list2)):
    if list2[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        list2[i] = '0' + list2[i]
print(list2)

import random

# list10 = list()
# while True:
#     a = random.randint(1, 33)
#     if a not in list10:
#         list10.append(a)
#         list10.sort()
#     if len(list10) == 6:
#         break
# list10.append(random.randint(1, 16))
#
# list20 = list(map(lambda x: str(x), list10))
# for i in range(len(list20)):
#     if list20[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#         list20[i] = '0' + list20[i]
# print(list20)

# list4 = list()
# import random
#
# while True:
#     a = random.randint(1, 33)
#     if a not in list4:
#         list4.append(a)
#         list4.sort()
#     if len(list4) == 6:
#         break
#
# list4.append(random.randint(1, 16))
#
# res = list(map(lambda x: str(x), list4))  #map 也是输入一个列表
# for i in range(len(res)):
#     if res[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#         res[i] = '0' + res[i]
#
# print(res)

# while 1 == 1:
#     a = random.randint(1, 33)
#     if a not in list4:
#         list4.append(a)
#         list4.sort()
#     if len(list4) == 6:
#         break
#
# list4.append(random.randint(1, 16))
# print(list4)

# import random
# list1=list()
# while 1:
#     a=random.randint(1,33)
#     if a not in list1:
#         list1.append(a)
#         list1.sort()
#     if len(list1)==6:
#         break
# list1.append(random.randint(1,16))
# print(list1)


# 求出1-2021年有多少个闰年
# i=1
# count2=0
# while i<=2021:
#     if (i %4 ==0) and (i %100 !=0) or (i %400 ==0) :
#         #print('%d 是闰年' % i)
#         count2 += 1
#
#     i=i+1
# print(count2)


# 求出1-100偶数的和
# i=1
# sum2=0
# while i<=100:
#     if i%2==0 :
#         sum2=sum2+i
#     i=i+1
# print(sum2)

# 求5-500所有奇数的和
# i=5
# sum3=0
# while i<=500 :
#     if i%2 ==1 :
#         sum3=sum3+i
#     i=i+1
# print(sum3)

# 打印1-100奇数的和
# sum3=0
# for i in range(1,101,2):
#     sum3= sum3+i
# print(sum3)

# a = [1, 2, 3, 4]
#
# b = map(lambda x: x * x, a)
#
# print(list(b))
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         print('*', end='')
#     print()
