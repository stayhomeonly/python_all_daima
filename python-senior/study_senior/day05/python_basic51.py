"""
==================================
文件名: python_basic51
作者:    星光梁朝伟
时间:   2022/5/15-10:22
==================================
"""
""""
for  循环 1.遍历可迭代数据 2.常和 range函数一起使用  除了number之外 其他的都是可以用for循环进行遍历

1.range
for 变量名 in range():
"""
# for i in range(5): # range 传单个入参（int） 生成一个 0到int-1的迭代器
#     print(i)
# for i in range(0, 5):
#     print(i)
# for i in range(1, 5):# 和切片类似 前包含后不包含
#     print(i)
# for i in range(1, 10, 2):
#     print(i)
# 用for 循环求1到100中所有奇数的和
sum1 = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         # sum1 += i
#         sum1 = sum1 + i
# print(sum1)

# for i in range(1, 101, 2):
#     sum1 = sum1 + i
#
# print(sum1)
# 用for循环求出1到1000 所有偶数的和
sum2 = 0
# for i in range(1, 1001):
#     if i % 2 == 0:
#         sum2 += i
# print(sum2)
for i in range(0, 1001, 2):
    sum2 += i
print(sum2)

print(sum(range(0, 1001, 2)))

eval()