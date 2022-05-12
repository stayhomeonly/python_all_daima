'''
---------------------------
File Name:calculator
Author:FENGXIN
date:2022/3/18-20:58

---------------------------

'''


class Math:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
