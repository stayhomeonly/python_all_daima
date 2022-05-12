"""
#@Time：2022/5/4-15:24
#@file：study1
#@Project:python_basic05.py
#@Content:

"""
# 9*9乘法表
import random

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}'.format(i, j, i * j), end=' ')
    print()

# 规则：**
# 1、双色球是由两种颜色的球（号码）组成,红色球：从1-33号球中，先择6个不重复的号码。
# 2、蓝色球：从1-16号球中，选择1个号码,从而组成的一个七位数的号码组合。
# 3、在显示的时候，红色球按照从小到到的顺序依次显示,用户从控制台输入一注双色球号码。
# 4、与计算机随机生成的双色球号码进行比对,判断用户中了几等奖。

# 自己购买的双色球
user_red_ball = []
user_blue_ball = []
count = 1
while True:
    if len(user_red_ball) == 6:
        break
    user_number = input('请输入第{}个数字:'.format(count))
    if not user_number.isnumeric():
        print('你输入的不是数字,请重新输入')
        continue
    user_number = int(user_number)
    if user_number < 1 or user_number > 33:
        print('你输入的数字不在范围，请重新输入')
        continue
    if user_number in user_red_ball:
        print('你输入的数字已经存在,请重新输入')
        continue
    user_red_ball.append(user_number)
    count = count + 1

user_red_ball.sort()

# 先制作一个奖池
number = 1
jiangchi = []
while number < 34:
    jiangchi.append(number)
    number = number + 1
print(jiangchi)
# 选择六个红球
red_ball = []

count1 = 1
while count1 <= 6:
    index = random.randint(0, len(jiangchi) - 1)  # 随机获取下标
    number = jiangchi[index]  # 通过随机下标获取数字
    red_ball.append(number)  # 数字就添加到红球里面
    del jiangchi[index]  # 删除掉已经奖池里面已经用过的数字，确保获取到的数字不重复
    count1 += 1
print(red_ball)
red_ball.sort()
# 蓝球
blue_ball = random.randint(1, 16)
print(blue_ball)
# 获取到一组双色球：
print('今天开奖的红色球是{}'.format(red_ball), end='')
print('{}'.format([blue_ball]))

# 自己购买的双色球
