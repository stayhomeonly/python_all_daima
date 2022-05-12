"""
=========================
File Name:python_baisic19
Author:冯鑫
Date:2021/11/22-11:24
==========================
"""

'''
本章讲解
1、死循环
2、while 循环使用else语句：
while 条件：
     条件 成立运行
else:当条件不成立，结束循环是运行
3、终止循环使用break 跳过本次循环，继续下次循环使用 continue
     
'''

'''
#常见的死循环

案例1：
i=1
while i<=100:
   print(i)
案列2：
i=1
while i<=100:
   if  i %2 ==0:
      print(i)
      i += 1   
'''

# 知识点2：whlie 循环使用else语句
i = 1
while i <= 100:
    print(i)
    i += 1
else:  # 循环完成后，循环条件不满足时，执行else下的语句块
    print(i)  # 11
    print('循环结束运行这里')

# 知识点3：终止循环使用break 跳过本次循环，继续下次循环使用 continue
i = 0
while i <= 10:
    i += 1
    if i == 5:
        # break #打印1，2，3，4 当i=5时，运行了break ，整个循环终止
        continue  # 打印1，2，3，4，6，7，8，9，10，11，当i=5时，跳过本次循环，进入到下一次

    print(i)

count1 = 0
while 1 == 1:
    count1 += 1
    print(count1)
    if count1 == 3:
        break
# 写个简单的登录：输入错误密码次数最多3次
# ct=0
# while True :
#     ct += 1
#     name = input('请输入用户名:')
#     password=input('请输入密码：')
#     if name =='xiaohua' and password =='123456':
#         print('登录成功')
#         break
#     else:
#         print('登录失败，输入次数还剩{}次'.format(3-ct))
#         if ct ==3 :
#             print('密码输入错误次数过多，账户已被锁定')
#             break

'''
for 循环
for 变量 in 可迭代数据（str/list/tuple/set/range().....)
    循环体
'''
# 知识点1：range()函数，前包含，后不包含
list1 = list(range(1, 4))
print(list1)  # [1,2,3]

for i in range(0, 5):  # 每一次循环会将，其中一个数字给i，直到所有的数据都给i为止
    print(i)  # 打印0，1，2，3，4
# 打印0-10的整数
for i in range(0, 11):
    print(i)

list2 = list(range(0, 12, 2))  # 这里的2代表步长，注意：12时最后的一个数，不包含
print(list2)  # [0, 2, 4, 6, 8, 10]

# 打印0-10的偶数
for i in range(0, 11, 2):  # 每循环一次，就把0-10步长为2的数字给i 注意：2是步长
    print(i)

# 打印1-2021年有多少闰年
count3 = 0
for i in range(1, 2022):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        count3 += 1
print(count3)
