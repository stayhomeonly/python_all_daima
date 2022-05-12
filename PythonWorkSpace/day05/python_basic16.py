"""
=========================
File Name:python_basic16
Author:冯鑫
Date:2021/11/19-15:24
==========================
"""

'''
本章讲解：分支嵌套
if 条件1：
    if 条件2：
       语句块3
     else：
        语句块4
 else:
    语句块2         
'''

# 西北玄天一朵云，乌鸦落进凤凰群，满桌都是英雄汉，谁是君来谁是臣

keyword = input('兄台，开始对暗号：西北玄天一朵云，下一句：')
if keyword == '乌鸦落进凤凰群':
    keyword2 = input('满桌都是英雄汉,下一句:')
    if keyword2 == '谁是君来谁是臣':
        print('组织欢迎你')
    else:
        print('拖出去，挂起来')
else:
    print('dadadadada')
