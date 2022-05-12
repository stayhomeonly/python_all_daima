"""
=========================
File Name:calculator
Author:冯鑫
Date:2021/11/25-13:59
==========================
"""
name = 'xiaohua'


# 加法
def add(x, y):
    return x + y


# 减法
def minus(x, y):
    return x - y


# 乘法
def mul(x, y):
    return x * y


# 除法
def division(x, y):
    return x / y


if __name__ == '__main__':  # 判断是否在当前模块运行(__name__在当前模
# 块下的值：__main__,在其他模块下值：day08.calculator)
    print(add(333, 666))  # 999
    print(name)
