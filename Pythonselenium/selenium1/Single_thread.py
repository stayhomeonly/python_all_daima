'''
---------------------------
File Name:Single_thread
Author:FENGXIN
date:2022/3/1-21:38

---------------------------

'''

from time import ctime, sleep


# 说
def talk():
    print("start talk:%r" % ctime())
    sleep(2)


# 写
def write():
    print("Start write %r" % ctime())
    sleep(3)


if __name__ == '__main__':
    talk()
    write()
    print('ALL end !%r' % ctime())
