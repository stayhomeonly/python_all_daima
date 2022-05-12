"""
=========================
File Name:thread
Author:冯鑫
Date:2021/12/8-17:34
==========================
"""
"""
进程是资源分配的最小单位,线程是cpu调度的最小单位

做个简单的比喻：进程=火车，线程=车厢

线程在进程下行进（单纯的车厢无法运行）
一个进程可以包含多个线程（一辆火车可以有多个车厢）
不同进程间数据很难共享（一辆火车上的乘客很难换到另外一辆火车，比如站点换乘）
同一进程下不同线程间数据很易共享（A车厢换到B车厢很容易）
进程要比线程消耗更多的计算机资源（采用多列火车相比多个车厢更耗资源）
进程间不会相互影响，一个线程挂掉将导致整个进程挂掉（一列火车不会影响到另外一列火车，但是如果一列火车上中间的一节车厢与前一节产生断裂，将影响后面的所有车厢）
进程可以拓展到多机，进程最适合多核（不同火车可以开在多个轨道上，同一火车的车厢不能在行进的不同的轨道上）
进程使用的内存地址可以上锁，即一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存。（比如火车上的洗手间）－"互斥锁"
进程使用的内存地址可以限定使用量（比如火车上的餐厅，最多只允许多少人进入，如果满了需要在门口等，等有人出来了才能进去）－“信号量”
"""

import threading
import time


def a():
    print('我要吃饭了!')
    time.sleep(1)  # 让当前线程等1s
    print('饭吃完了!')


def b():
    print('找对象聊聊天!')
    time.sleep(1)
    print('聊完了')


def c():
    print('我要追星,我要上微博给爱豆点赞!')
    time.sleep(1)
    print('追星成功~')


start_time = time.time()  # 获取当前时间戳
a(), b(), c()  # 调用三个函数
end_time = time.time()
print('总耗时:{}'.format(end_time - start_time))

print('===' * 50)


def a1():
    print('我不吃饭了!', end='')
    time.sleep(1)  # 让当前线程等1s
    print('以后都不吃了!', end='')  # 一旦进行多线程同时运行，顺序不分先后了


def b1():
    print('找不到对象!', end='')
    time.sleep(1)
    print('再努努力~', end='')


def c1():
    print('再也不追星了!', end='')
    time.sleep(1)
    print('爱豆跑早操去了~', end='')


start_time = time.time()

t1 = threading.Thread(target=a1)
t2 = threading.Thread(target=b1)
t3 = threading.Thread(target=c1)

t1.start()  # 启动线程,当前运行的程序代表主线程,t1,t2,t3代表子线程
t2.start()
t3.start()

end_time = time.time()
print('多线程总耗时:{}'.format(end_time - start_time))
