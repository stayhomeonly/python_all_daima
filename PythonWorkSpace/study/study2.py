"""
#@Time：2022/5/17-17:23
#@file：study2
#@Project:python_basic05.py
#@Content:

"""
try:
    num = int(input('请输入一个数字：'))
    print(100 / num)
except ZeroDivisionError:#如果try中的代码出现ZeroDivisionError，则执行except语句块
    print('请您输入一个非0的数字')
else:
    print('没有出现异常！')#如果try中的代码没有出现异常，则执行else语句块
finally:
    print('执行完成！')