"""
=========================
File Name:python_basic29
Author:冯鑫
Date:2021/11/25-14:02
==========================
"""
import day08.calculator as cal

'''
模块导入：当前模块导入其他模块的内容，我们就可以使用该模块的变量或者函数
模块导入方式
导入整个模块方式：impotr 包名.模块名 as 别名
'''

print(cal.name)  # xiaohua 访问calculator 模块下的name变量
print(cal.add(100, 300))  # 400 访问calculator 模块下的add方法
print(cal.division(10, 5))  # 2.0 访问calcultor 模块下的division方法

print(__name__)  # __main__
print(cal.__name__)  # day08.calculator
