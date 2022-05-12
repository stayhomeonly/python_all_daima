"""
=========================
File Name:python_basic25
Author:冯鑫
Date:2021/11/23-16:59
==========================
"""

'''
函数参数的定义：
1、必须参数（位置参数）
2、默认参数
3、不定长参数（可变参数）
4、关键字参数
'''
'''
#1、必须参数（位置参数）：入参按照位置传递，在调用时入参的元素个数必须时相同的
'''


def fun1(a, b, c):
    return a, b, c


# 调用方式1：自动按位置赋值
print(fun1(1, 2, 3))  # (1, 2, 3)

# 调用方式2：相当于在调用的时候，直接声明给某个入参XX值
print(fun1(b=2, a=5, c=10))  # (5, 2, 10) 相当于把2赋值给fun1中的变量b 把5赋值fun1的变量a，把10赋值给fun1中的c

'''
# 2、默认参数：在声明函数的时候给入参设置默认的值，如果只传入一个值，那么b使用
默认值，那么b使用传入的值
'''


def fun2(a, b=10):  # 这里a时必须参数，b是默认参数，默认值为10
    return a + b


res = fun2(5)  # 把5赋值给a,b使用的默认值
print(res)  # 15

res2 = fun2(50, 100)  # 把50赋值给a  把100赋值给b
print(res2)  # 150

'''
3、不定长参数(可变参数)：可以存入0-N个入参，一般声明的时候使用*args,调用该方法
时如果传入多个入参，会自动组包成一个元组
'''


def fun3(*args):
    print('入参为', args)


fun3()  # 入参为
fun3(1)  # 入参为（1，）
fun3(1, 2, 3, 4, 5, 6, 7, 8, 9)  # 入参为 (1, 2, 3, 4, 5, 6, 7, 8, 9)


# 使用不定长参数声明一个函数，求这些入参的和，并且调用该函数
def fun4(*args):  # 接收多个参数并且将他们打包成元组
    return sum(args)  # 求元组的和


print(fun4(1, 2, 3))  # 6
print(fun4())  # 0
print(fun4(1))  # 1

'''
4、关键字参数：用来接受key-values 格式的入参，保存为一个字典
'''


def fun5(**kwargs):  # 两颗星星表示，将传入的多个键值对打包成一个字典
    print('参数为', kwargs)


fun5(a=1, b=2, c=3)  # 调用该方法后，打印出来一个字典fun5(a=1,b=2,c=3)    #调用该方法后，打印出来一个字典
# fun5(1)会报错，只使用关键字参数接收数据时，必须传入键值对数据
fun5(name='xiaohua', age=18, sex='女')  # 参数为 {'name': 'xiaohua', 'age': 18, 'sex': '女'}

'''
5、多种参数混合使用
'''


# 案列
def test(x, y=5, z=6, *args, **kwargs):
    print('x的值是{},y的值是{},z的值是{},args的值是{},kwargs的值是{}'.format(x, y, z, args, kwargs))


test(1)  # x的值是1,y的值是5,z的值是6,args的值是(),kwargs的值是{}
test(1, 2)  # x的值是1,y的值是2,z的值是6,args的值是(),kwargs的值是{}
test(1, 2, 3, 4, 5, 6, 7)  # x的值是1,y的值是2,z的值是3,args的值是(4, 5, 6, 7),kwargs的值是{}
test(1, 2, 3, 4, 5, 6, 7, a=4, b=4)  # x的值是1,y的值是2,z的值是3,args的值是(4, 5, 6, 7),kwargs的值是{'a': 4, 'b': 4}
# test(1,2,3,4,5,6,7,x=4,b=4)TypeError: test() got multiple values for argument 'x'
test(1, z=3)  # x的值是1,y的值是5,z的值是3,args的值是(),kwargs的值是{}


# 案列2：
def test2(*args, **kwargs):
    print('args的值是{},kwargs的值是{}'.format(args, kwargs))


test2(1, 2, 3)  # args的值是(1, 2, 3),kwargs的值是{}
test2(a=1, b=1)  # args的值是(),kwargs的值是{'a': 1, 'b': 1}
test2(1, 2, 3, 4, 5, 6, a=1, b=2)  # args的值是(1, 2, 3, 4, 5, 6),kwargs的值是{'a': 1, 'b': 2}


# 声明一个函数，可以判断是否为闰年
def fun10(a):
    if a % 4 == 0 and a % 400 != 0 or a % 100 == 0:
        print('{}是闰年'.format(a))
    else:
        print('{}不是闰年'.format(a))


fun10(2013)


# 声明一个函数入参行数和列数可以打印出对应的矩形
def fun12(a, b):
    for i in range(a):
        for j in range(b):
            print('*', end='  ')
        print()


fun12(10, 8)

'''       
************
************
************
************ 
'''


# 声明一个函数sort1() 功能是可以进行排序，可控制正反序
def sort2(list3, reverse=True):
    if reverse:
        for i in range(len(list3) - 1):
            for j in range(len(list3) - 1 - i):
                if list3[j] > list3[j + 1]:
                    list3[j], list3[j + 1] = list3[j + 1], list3[j]
    else:
        for i in range(len(list3) - 1):
            for j in range(len(list3) - 1 - i):
                if list3[j] < list3[j + 1]:
                    list3[j], list3[j + 1] = list3[j + 1], list3[j]
    print()


list3 = [2, 3, 444, 5555, 1, 0]
sort2(list3)
print(list3)
# sort2(list3,reverse=False)
# print(list3)


#
# def sort1(list1,reverse=False):
#     if reverse:
#         for i in range(len(list1) - 1):
#             for j in range(len(list1) - 1 - i):
#                 if list1[j] > list1[j + 1]:
#                     list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     else:
#         for i in range(len(list1) - 1):
#             for j in range(len(list1) - 1 - i):
#                 if list1[j] < list1[j + 1]:
#                     list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     print()
# list1 = [1, 2, 44, 55, 7, 9]
# sort1(list1)
# print(list1)
# sort1(list1,reverse=True)
# print(list1)
