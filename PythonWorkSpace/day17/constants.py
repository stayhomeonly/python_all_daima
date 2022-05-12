"""
=========================
File Name:constants
Author:冯鑫
Date:2021/12/8-12:01
==========================
"""

import os

'''
使用常量对路径进行管理
好处：代码使用非绝对路径，可移植性高
'''

path = os.path.dirname(__file__)  # 获取当前的目录
print(path)  # D:/PythonWorkSpace/day17

path = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的父级目录
print(path)  # D:/PythonWorkSpace
