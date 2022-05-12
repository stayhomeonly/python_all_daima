"""
=========================
File Name:python_basic03.py
Author:冯鑫
Date:2021/11/15-14:24
==========================
"""
'''
本章讲解；变量的声明
注意：等于号=不是相等的意思，等于号是一个赋值的符号
'''
py = '你好'
print(py)  # 你好
# 声明变量,变量时用来储存值的

# ************* 知识点1：变量的声明
a = 1  # 该行代码声明一个变量a,将1赋值给a,且a的类型为整数类型变量
b = 2.2  # 改行代码声明一个变量b，将2.2赋值给b，且b的类型为浮点数类型（小数）

print(a)  # 1
print(b)  # 2.2
print(a + b)  # 3.2
name = 'xiaohua'  # 声明了一个变量name,将'xiaohua'赋值给name，那么name变量的类型是字符串类型
print('name的值是:', name)  # name的值是：xiaohua  注意： 这个,会将'name的值是:'和name

# ***********************知识点2：变量的覆盖，变量可以一次声明，多次赋值，后面的赋值会覆盖前面的值
sal = 1000  # 声明sal变量，并且赋值1000
sal = 2000  # 为sal变量重新赋值2000
print(sal)  # 2000

sal = sal + 1000  # 先运行sal+1000,在把运算的结果赋值给sal
print(sal)  # 2000

s = 'xiaohua'  # 声明一个变量s,为该变量赋值为'xiaohua'
print(s)  # xiaohua

# ********************知识点3：同时为多个变量赋值
a = b = c = 1  # 该行代码声明了a,b,c三个变量，且赋值为1
print(a, b, c)  # 1,1,1

d, e, f = 1, 'xiaohua', 15.5  # 声明三个变量d,e,f,并且把值1，xiaohua,15.5分别赋值他们
print(d, e, f)

# *****************知识点4：在python里面是严格区分大小写的
sno = 1001
Sno = 1002  # sno与Sno并不是同一个变量，所以这里不产生覆盖
print('sno的值:', sno)  # sno的值:1001
print('Sno的值:', sno)  # Sno的值:1002

# ******************* 知识点5：变量的声明不能使用哪些标识

# 1=1 不能使用数字做变量名
# sa$1=100 $是特殊符号，变量名中不能包含特殊符号，除了下划线
sal1 = 1000
print(sal1)
sa_l = 100
print(sa_l)  # 100

# ctrl+/ 自动在最前面加上#号键，让其不运行

# and=1 and是关键字，也不能作为变量名
# 查看python里面有哪些保留字（关键字）
import keyword

print(keyword.kwlist)  # 打印python里面的所有保留字
'''
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield'
'''
