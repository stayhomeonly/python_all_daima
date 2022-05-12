"""
=========================
File Name:python_basic33
Author:冯鑫
Date:2021/11/25-20:03
==========================
"""
'''
错误和异常的区别
错误：不能通过解释器的编译，这种叫错误
异常：编译通过，运行时
'''
# 常见的错误
#  print('hello')#IndentationError: unexpected indent
# print( # 语法错误SyntaxError: unexpected EOF while parsing

# 常见的异常
# print(10/0)#除0异常ZeroDivisionError: division by zero
list1 = [1, 2, 3, 4]
# print(list1[4])#下标越界异常 IndexError: list index out of range

# with open(r'./test1.txt',mode='r',encoding='utf8') as fr:
#     print(fr.read())# 找不到异常文件 FileNotFoundError

num = int(input('请输入一个数字：'))
print(100 / num)
