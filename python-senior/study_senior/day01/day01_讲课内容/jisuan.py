'''
---------------------------
File Name:jisuan
Author:FENGXIN
date:2022/4/17-16:27

---------------------------

'''
# 设计一个两位数加法的计算器，用户输入两位数字，打印出两位数字的和
# a = int(input("请输入第一位数字:"))
# b = int(input("请输入第一位数字:"))
# print(a+b)


# while 1:
#     a = int(input("请输入第一位数字:"))
#     while a < 10 or a > 99:
#         print("输入的不是两位数,请重新输入:")
#         a = int(input("请重新输入第一位数字:"))
#
#
#     # elif type(a) is not int or float:
#     #     print()
#
#     b = int(input("请输入第二位数字:"))
#     while b < 10 or b > 99:
#         print("输入的不是两位数,请重新输入:")
#         b = int(input("请重新输入第二位数字:"))
#
#     print(a + b)
#     break
# 解决浮点数类型的方法：decimal
from decimal import Decimal

c = Decimal('4.2')
d = Decimal('3.4')
print(c + d)
