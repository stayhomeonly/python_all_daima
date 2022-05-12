# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/6-14:42
=============================
"""

# input函数讲解


# input() 这个函数用来读取控制台的输入，可以接收控制台输入内容，并且保存到变量里
name = input('请输入您的姓名:')  # 变量name接收input()函数输入数据
print('您输入的姓名是:', name)  # 您输入的姓名是: 刘老师
print(type(name))  # <class 'str'>

age = input('请输入您的年龄:')  # input()函数读取的所有从控制台输入的内容都是字符串类型
print('姓名是:', name, '年龄是:', age)
print(type(age))  # <class 'str'>

# 设计一个简单的两位整数加法运算器,直接讲不做为练习题
num1 = input('请输入第一个整数:')
num2 = input('请输入第二个整数:')
sm = int(num1) + int(num2)
print('两个整数之和是:', sm)
