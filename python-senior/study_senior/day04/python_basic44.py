"""
==================================
文件名: python_basic44
作者:    xiaoliu
时间:   2022/5/8-15:18
==================================
"""
"""
1.while 循环使用else语句：  在while……else，当循环判定条件为False时执行else语句块
while 条件：
    语句块
else:
    语句块
当循环结束时，会执行else
2.终止循环使用break，会直接停掉循环不会执行后面循环体的代码
3.跳过本轮循环使用continue，跳过后不会再执行后面的代码，会直接进入下一次循环
4.死循环
"""

# 案例1
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("循环已经结束！")

i = 0
while i <= 10:
    i += 1
    if i == 5:
        # break  # 打印结果： 1、2、3、4
        continue  # 打印结果：
    print(i)

print('=' * 50)

# 登录：最多用户名密码错误3次，用户名为 scott 密码为 1234，密码错误会提示剩余次数
# count = 3
# while True:  # 非0为真，非空为真
#     username = input("请输入用户名：\n")
#     pwd = input("请输入密码：\n")
#     if username == 'scott' and pwd == '1234':
#         print("登录成功！")
#         break
#     else:
#         count -= 1
#         if count <= 0:
#             break
#         else:
#             print("登录失败,您还有{}次机会".format(count))

# 课堂小练习：
# 水仙花数是指一个 n 位数(n≥3)，它的每个位上的数字的 n 次幂之和等于它本身（例如：1**3 + 5**3 + 3**3 = 153）。
# 求1000以内所有的水仙花数
#  取值范围 100-999

narcissus = 100
while narcissus < 1000:
    # 获取百位
    a = narcissus // 100
    # 获取十位
    b = narcissus % 100 // 10
    # 获取个位
    c = narcissus % 10
    if a ** 3 + b ** 3 + c ** 3 == narcissus:
        print(narcissus)
    narcissus += 1

