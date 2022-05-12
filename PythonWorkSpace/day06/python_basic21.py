"""
=========================
File Name:python_basic21
Author:冯鑫
Date:2021/11/22-16:25
==========================
"""

'''
循环嵌套
'''
for i in range(5):  # 外循环5次
    for j in range(5):  # 每次外循环，执行5次内循环
        print(i, j)  # 总共打印25次

# 打印一个5行5列的矩形

# for i in range(5):
#     print('*****')
# 如何只用一个* 如何实现每次循环打印5个 * 而且不换行,做成矩形
for i in range(5):  # i=0外循环一轮  i=1外循环第一轮
    for j in range(5):  # j=0,1,2,3,4   j=0,1,2,3,4   .....
        print('*', end='')
    print()

# 打印一个4行直角三角型
# for i in range(0,4):
#     for j in range(0,i+1):
#         print('*',end='')
#     print()
#
# print('*')
# print('**')
# print('***')
# print('****')

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{} ={}'.format(i, j, i * j), end='  ')
    print()

# 打印9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='  ')
#     print()
