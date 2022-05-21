"""
#@Time：2022/5/20-21:18
#@file：python_basic02
#@Project:python_basic05.py
#@Content:

"""
# 参测女人的年纪
black_girl_age=26
# for i in range(3):
#     guess=int(input("输入你的猜测:"))
#     if guess>black_girl_age:
#         print("我哪有这么老")
#     elif guess <black_girl_age:
#         print('我哪有这么年轻')
#     else:
#         print('恭喜你猜对了，可以把我领回家')

# 但是上面的程序与一个弊端，哪怕你是第一次就猜对了年龄也还是要进行循环3次，所以要优化
for i in range(3):
    guess=int(input("输入你的猜测:"))
    if guess>black_girl_age:
        print("我哪有这么老")
    elif guess <black_girl_age:
        print('我哪有这么年起')
    else:
        exit('恭喜你猜对了，可以把我领回家') # 就是把最后一个代码直接从print改为exit，猜对了直接退出程序

