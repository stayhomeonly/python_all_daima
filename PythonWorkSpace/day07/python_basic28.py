"""
=========================
File Name:python_basic28
Author:冯鑫
Date:2021/11/24-17:14
==========================
"""

'''
内置函数：python自带的高级内置函数
'''
# 常用的内置函数：print()/len()/max()/min()/sum()/id()/type().....

# 1、eval():识别字符串中的python的表达式，并且进行运算
print('1+1')  # 1+1
print(eval('1+1'))  # 2 eval()将字符串中的表达式识别为1+1，并且进行计算
eval('print("hello world")')

# num1=input('请输入第一个数字:')
# num2=input('请输入第二个数字:')
# print(eval(num1)+eval(num2))#类似于print(eval('num1+num2'))

# 输出一个列表，并且求出列表的和
# list1=input('请输入一个列表:') #[1,2,3,4,5]
# print(sum(eval(list1))) #15

# 2.exec() 可以识别相对复杂的表达式 eval()识别简单的表达式
# 有返回值时，使用eval,无返回值时exec()
str1 = '''
def fun1():
    print('Hello')

'''
# eval(str1) 该行代码报错，eval()函数识别相对简单的表达式
exec(str1)  # exec()识别str1字符串中的fun1()函数
fun1()  # Hello

# 3.filter() 自定义过滤，filter用来过滤序列，过滤掉不符合条件的成员，返回条件符合的成员
list2 = [10, 20, 30, 40, 50, 60, 100]


# filter过滤出list2中大于40的值
# 第一步：写出一个过滤条件
def fun2(x):
    return x > 40


# 第二步：使用filter过滤
print(list(filter(fun2, list2)))  # [50, 60, 100]

# filter()需要传2个参数，第一个是函数名，第二个是序列
# 把后面的可迭代的序列中的每一个成员传给前面的函数，返回True或False，
# 并且把返回为True的成员放到一个迭代器里面使用（最好转换成一个列表）

# filter 同如下逻辑
list3 = []
for i in list2:
    if i > 40:
        list3.append(i)
print(list3)

# 使用filter() 函数过滤元组中的偶数
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 98, 9, 10)


# def fun12(x):
#     if x %2 ==1:
#         return x

def fun12(x):
    return x % 2 == 0


print(tuple(filter(fun12, tup1)))
print(tuple(filter(lambda x: x % 2 == 0, tup1)))

# # 使用lambda表达式
# print(tuple(filter(lambda x : x % 2 == 0, tup1)))#(2, 4, 6, 8, 98, 10)
#
# # 4.map() 把后面的可迭代的序列中的每一个成员传给前面的函数，是把结果直接放到迭代器里（最好转换成列表使用)
print(tuple(map(fun12, tup1)))
print(tuple(map(lambda x: x % 2 == 0, tup1)))

# lambda a,b : a%b 前面是入参数，中间是：后面是函数体
# filter(fun15,list12)

# 5.zip() 聚众打包，当需要打包的对象长度不统一时，按最短的来
list1 = ['name', 'age', 'sex', 'class']
list2 = ['xiaohua', 20, '女', 23]
list3 = [1, 2, 3]
print(dict(zip(list1, list2)))  # {'name': 'xiaohua', 'age': 20, 'sex': '女', 'class': 23}
print(list(zip(list1, list2, list3)))  # [('name', 'xiaohua', 1), ('age', 20, 2), ('sex', '女', 3)]

# 底层逻辑
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)  # {'name': 'xiaohua', 'age': 20, 'sex': '女', 'class': 23}

# 判断一个字符串中是否为纯数字
str2 = '1232154325'
print(str2.isnumeric())

is_ture = '纯数字'
for i in str2:
    if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        is_true = '不是纯数字'
        break
print(is_ture)
