"""
=========================
File Name:python_basci30
Author:冯鑫
Date:2021/11/25-14:31
==========================
"""
from day08.calculator import name,mul,division

'''
模块导入方式2：导入某个模块下的部门内容(不推荐使用，如果导入多个文件可能存在相同
的方法情况，造成意想不到的bug)
格式：from 包名.模块名 import 函数名1，函数名2，变量名......
'''

print(name) #xiaohua
print(mul(666,222))#147852
print(division(666,222))#3.0