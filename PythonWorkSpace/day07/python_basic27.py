"""
=========================
File Name:pthon_basic27
Author:冯鑫
Date:2021/11/24-17:14
==========================
"""

'''
函数传递值的方式：值传递和引用传递

值传递：传递的是变量的值而非变量本身，被传递的变量的值不会被改变
引用传递：传递的是变量本身，被传递的变量的值会被改变

注意：
可变类型(列表，集合，字典)(list/set/dict)  引用传递
不可变类型（数字，字符，元祖）(int/str/tuple) 值传递
'''


def fun1(a):
    a += 1
    print(a)


a = 10
fun1(a)  # 11 值传递 调用fun1()函数，并且把a的值10 传给fun1的入参a
print(a)  # 10


def fun2(list1):
    list1.append(5)
    print(list1)


list2 = [1, 2, 3, 4]
fun2(list2)  # [1,2,3,4,5]
print(list2)  # [1, 2, 3, 4, 5] 可变类型是引用传递，传递的整个空间物理地址，增加的内容会一起传递过来

'''
使用lambda 实现简单功能的函数
语法：lambda[arg1,arg2........]:函数体
'''


def fun3(a, b):
    return a % b


print(fun3(1, 2))  # 1
# 使用lambda 实现上面的函数
fun4 = lambda a, b: a % b  # 入参a,b 函数体是a%b
print(fun4(1, 2))  # 1


# 写一个函数判断是否为偶数：
def fun5(m):
    if m % 2 == 0:
        return '偶数'
    else:
        return '奇数'


fun6 = lambda m: m % 2 == 0  # 入参是num,函数体是m%2
print(fun6(12))  # True

