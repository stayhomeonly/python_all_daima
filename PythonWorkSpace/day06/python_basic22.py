"""
=========================
File Name:python_basic22
Author:冯鑫
Date:2021/11/22-19:57
==========================
"""

'''
冒泡排序
'''
# 数据交换，将a和b的值交换
a = 1
b = 2

# t=a
# a=b
# b=t
a, b = b, a
print(a, b)

# 有int类型的列表[3,7,4,9]交换下标0和下标1的值
# list1=[3,7,4,9]
# list1[0],list1[1]=list1[1],list1[0]
# print(list1) #[7, 3, 4, 9]

# 使用冒泡排序对列表进行从小到大排序
# list1 = [30, 50, 20, 70, 6]
# for i in range(len(list1) - 1):
#     for j in range(len(list1) - 1 - i):
#
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)


# 如果前面的值必后一位的值大，就让他们交换位置
# 每一轮大循环，都可以将一个值放到正确的位置，那么长度为5的列表需要放4次，所以大循环需要4次
# 五个数需要比较四次，才能将最大的值放在后面
# for i in range(len(list1)-1) :
#     if list1[i]>list1[i+1]:
#         list1[i],list1[i+1]=list1[i+1],list1[i]
#     print(list1) 一个外循环和内循环

# 第一轮外循环 i=0 j=0[30,50,20,70,6] j=1[30,50,20,70,6],j=2[30,20,50,70,6] j=3[30,20,50,6,70]
# 第二轮外循环i=1 j=0[20,30,50,6,70] j=1[20,30,50,6,70] j=2[20,30,6,50,70]
# 第三轮外循环i=2 j=0[20,30,6,50,70],j=1[20,6,30,50,70]
# 第三轮外循环i=2 j=0[6,20,30,50,70]


# for i in range(len(list1) - 1):
#     for j in range(len(list1) - 1 - i):
#
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     print(list1)

# 从大到小进行冒泡排序
# list1=[3,7,9,1,5,5,6,6]
# for i in range(len(list1)-1):
#     for j in range(len(list1)-1-i):
#         if list1[j] < list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j+1],list1[j]
# print(list1)


# 冒泡排序核心：
# 每循环一次，确定一个位置，就是比较序列中两个元素的大小进行排序
# 从小到大时：如果前面的元素比后面大，就进行位置交换
# 从大到小时：如果前面的元素比后面小，就进行位置交换
