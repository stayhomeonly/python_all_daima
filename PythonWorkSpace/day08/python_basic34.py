"""
=========================
File Name:python_basic34
Author:冯鑫
Date:2021/11/25-20:13
==========================
"""
'''
异常处理
try:
   语句块1
except  异常类型1
      语句块2
except 异常类型2
     语句块3
[else]:else是可选内容，如果没有异常，则执行else语句块内容
[finally] :finally 是可选内容，不管有没有内容，都必须执行

执行try中的语句块，如果语句块1出现了异常1则执行语句块2             
'''

# try:
#     num = int(input('请输入一个数字：'))
#     print(100 / num)
# except ZeroDivisionError:#如果try中的代码出现ZeroDivisionError，则执行except语句块
#     print('请您输入一个非0的数字')
# else:
#     print('没有出现异常！')#如果try中的代码没有出现异常，则执行else语句块
# finally:
#     print('执行完成！')

'''
分别处理多种异常
'''
# try:
#     num=int(input('请输入一个数字：'))
#     print(100 / num)
# except ZeroDivisionError:  # 如果try中的代码出现ZeroDivisionError，则执行except语句块
#     print('请您输入一个非0的数字')
# except ValueError:
#     print('请您输入正确的数字！')
#
#
# ''' 同时处理多种异常'''
# try:
#     num=int(input('请输入一个数字：'))
#     print(100/num)
# except(ZeroDivisionError,ValueError) :#如果try中出现ZeroDivisionError,ValueError，则执行except
#     print('请输入正确的数据！')


# '''
# 万能处理异常方式
# '''
# try:
#     num = int(input('请输入一个数字：'))
#     print(100 / num)
# except Exception  as  e:#如果try中出现了excepetion，则执行exceptd下的语句块
#     print('请输入正确的数据！',e)#e代表报错信息
