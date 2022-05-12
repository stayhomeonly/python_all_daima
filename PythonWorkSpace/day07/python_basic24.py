"""
=========================
File Name:python_basic24
Author:冯鑫
Date:2021/11/23-11:50
==========================
"""

'''
函数：函数是可以重复使用的一段代码 比如：print() /id ()/type()/input()/len()
函数的定义规则
def 函数名（参数1，参数2，参数3.....) 也可能没有参数
    函数体（用来实现XXX功能)
    [return]代表结束函数且返回数据 也肯能没有return
'''
'''
1、无入参，无返回
'''


def fun1():  # 声明一个函数，名字叫做fun1，没有入参，没有返回
    print('这个函数被调用了')


fun1()  # 调用了fun1的函数
'''
2、有入参，无返回
'''


def add1(a, b):  # 声明了一个函数，函数名add1，需要2个参数，没有返回，调用该函数时必须入参2个参数
    print(a + b)


add1(1, 2)  # 3 调用了add1函数，并且传入了两个参数
add1(666, 888)  # 1554 函数可以多次条用
'''
3、有入参，有返回
'''


def add2(a, b, c):  # 声明了一个函数，函数的名字叫做add2,需要三个参数，有返回值，调用该函数是必须传入3个参数
    return a + b + c


res1 = add2(1, 2, 3)  # 这个函数是有返回，所有我们可以设定一个变量去接受他的结果
print(res1)  # 6
print(add2(10, 30, 50))
print(add2('a', 'b', 'c'))  # abc

'''
4、无入参，有返回
'''


def fun2():
    return 1


print(fun2())

'''
函数的声明
'''


# 设计一个函数，有两个入参，该函数可以返回矩形的面积
def mj1(chang, kuan):
    return chang * kuan


res1 = mj1(4, 3)
print(res1)


# 声明一个函数，用来判断奇数还是偶数，并且返回判断结果
def fun10(num):
    if num % 2 == 0:
        return "{}是偶数".format(num)
    else:
        return "{}是奇数".format(num)


num1 = 15
print(fun10(15))  # 15是奇数


# 设计一个函数，入参一个成绩列表，返回班级的总成绩，平均成绩，最高成绩，最低成绩
def fun4(list12):
    return sum(list12), sum(list12) / len(list12), max(list12), min(list12)


list12 = [100, 90, 50, 60, 30]
print(fun4(list12))


# 函数返回多个值
def math(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c, d, e, f  # 如果返回多个值，会自动把多个值打包成一个元组


res3 = math(10, 20)
print(res3)  # (30, -10, 200, 0.5)

num1, num2, num3, num4 = math(10, 20)  # 自动拆包
print(num1, num2, num3, num4)  # 30 -10 200 0.5


# 声明一个函数，需要传入一个保存了很多个人成绩的元组，该函数返回元组中所有成绩的和
def sum_score(tup):
    return sum(tup)
