"""
#@Time：2022/5/8-16:23
#@file：study2
#@Project:python-senior
#@Content:

"""
# 课堂小练习：
# 水仙花数是指一个 n 位数(n≥3)，它的每个位上的数字的 n 次幂之和等于它本身（例如：1**3 + 5**3 + 3**3 = 153）。
# 求1000以内所有的水仙花数
list1 = []
for i in range(100, 1000):
    # 百位数上的数字
    a = str(i)[0]
    # 十位数上的数字
    b = str(i)[1]
    # 各位上的数字
    c = str(i)[2]
    if int(a) ** 3 + int(b) ** 3 + int(c) ** 3 == i:
        print(i)
        list1.append(i)

    i = i + 1
print(list1)

for i in range(100, 1000):
    # 百位数上的数字
    a1 = i // 100
    # 十位数上的数字
    b2 = i % 100 // 10
    # 个位数的数字
    c2 = i % 10
    if a1 ** 3 + b2 ** 3 + c2 ** 3 == i:
        print(i)
    i = i + 1


