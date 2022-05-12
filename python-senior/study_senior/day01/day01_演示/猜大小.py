# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2022/1/15-11:23
=============================
"""
import random

# 练习1：猜大小
# 规则:1.有三个骰子,每个骰子大小从1-6,用户可以可以输入 押注金额 和 竞猜内容:大、小
#     2.随机生成三个骰子大小,并且求出他们的和sum,sum为3-9是小,sum为10-18是大
#     3.如果用户猜对了,得到双倍奖金，如果猜错了则输掉押注金额

while True:
    # 输入初始兑换筹码
    chip = int(input('请输入要兑换的筹码:\n'))
    if chip <= 0:
        print('您的输入有误,请重新输入!')
    else:
        break

# 显示余额开始游戏
print('账户余额是:%d,祝您玩的开心~' % chip)

while True:
    # 筹码为0 游戏结束
    if chip <= 0:
        break

    # 押注金额大于筹码则重新输入
    bet = int(input('请输入您要下注的筹码:\n'))
    if bet <= 0:
        print('您的输入有误,请重新输入!')
        continue
    if bet > chip:
        print('您输入的筹码大于余额,您还剩%d,请重新输入:\n' % chip)
        continue

    # 点数非'大'或'小'则重新输入
    decision = input('请输入大小,3-9是小、10-18是大:\n')
    if decision not in ('大', '小', 'da', 'xiao', 'd', 'x'):
        print('您的输入有误,请重新输入押注筹码和点数"大"或"小":\n')
        continue

    # 扣除押注金额
    chip -= bet

    # 开始摇色子
    res = 0
    for i in range(3):
        res += random.randint(1, 6)

    # 猜中给予双倍奖金,猜错给予鼓励
    if 3 <= res <= 9 and decision in ('小', 'xiao', 'x'):
        bet *= 2
        chip += bet
        print('点数是:%d,恭喜您猜对了!获得双倍奖金,余额:%d' % (res, chip))
    elif 10 <= res <= 18 and decision in ('大', 'da', 'd'):
        bet *= 2
        chip += bet
        print('点数是:%d,恭喜您猜对了!获得双倍奖金,余额:%d' % (res, chip))
    else:
        print('点数是:%d,很遗憾您猜错了,再接再厉哦!余额:%d' % (res, chip))

    # 余额不足时踢出游戏
    if chip == 0:
        print('您已经没有筹码了,欢迎下次来玩哦~~')
        break

    # 每局结束确认是否继续游戏
    play = input('输入"Y"或任意内容继续游戏,输入"N"退出游戏!\n')
    if play in ('N', 'n'):
        print('还剩%d余额,下次再来玩哦~' % chip)
        break
    else:
        continue
