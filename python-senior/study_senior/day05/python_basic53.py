"""
==================================
文件名: python_basic583
作者:    星光梁朝伟
时间:   2022/5/15-14:13
==================================
"""
"""
循环嵌套 ：循环里面 还有循环
"""
# print(1, 2, end=' ')
# print(3)
#
# # 打印4行星星
# print('****')
# print('****')
# print('****')
# print('****')
# print('-' * 50)
# for i in range(4):  # 0123
#     print('****')
# 打印一个直角三角形
# 实例
# *
# **
# ***
# ****
for i in range(4):  # 0123 外循环一次 内循环全部执行完
    for j in range(i + 1):
        print('*', end='')  # 执行了10次
    print()  # 执行了4次
print('==' * 50)
# 输出99乘法表
for a in range(1, 10):  # 123456789
    for b in range(a):
        print('{}*{}={}'.format(b + 1, a, (b + 1) * a), end=' ')
    print()
print('---' * 10)
for i in range(9):  # 012345678
    for c in range(i + 1):
        print('{}*{}={}'.format(c + 1, i + 1, (c + 1) * (i + 1)), end=' ')
    print()
