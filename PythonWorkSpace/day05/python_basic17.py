"""
=========================
File Name:python_basic17.
Author:冯鑫
Date:2021/11/19-16:16
==========================
"""

import random

# (import 引入，random 随机）
str1 = 'abcdef'
print(random.choice(str1))  # 随机选择序列中一个元素

num = random.randint(1, 10)  # 随机选择1-10之间的数字
num2 = random.randint(5, 20)  # 随机选择5-20之间的数字

print(num)
print(num2)
