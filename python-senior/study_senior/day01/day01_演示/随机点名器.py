# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/11/23-12:18
   content:随机数
=============================
"""
#
import random

# 随机一个骰子
p_count = random.randint(1, 7)  # 随机一个整数，前包含后不包含，所以随机出来的数字为1到6
print(p_count)

# 随机班级点名器
names = ['小花', '小王', '小张', '小李']
print(random.choice(names))
