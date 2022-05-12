"""
=========================
File Name:test_ddt01
Author:冯鑫
Date:2021/12/4-17:06
==========================
"""
'''
ddt 可以在参数化测试数据，把不同的数据进行参数化，做到代码逻辑和测试数据分离
使用方法：
1、将测试类使用@ddt进行标记
2、将需要循环使用测试数据的测试方法，用@data进行标记
'''
import unittest
from ddt import ddt, data


# 不使用ddt测试add()的函数
def add(a, b):
    return a + b


# 不使用ddt、unittest第三方测试包进行测试,需要查看控制台输出的结果，比较雷
res = add(1, 2)
print(res)  # 3

res1 = add(-1, -3)
print(res1)  # -4


# 使用unittest 测试，进行自动对比
class TestAdd(unittest.TestCase):
    def test01(self):
        res2 = add(1, 2)
        self.assertEqual(3, res2)

    def test02(self):
        res3 = add(-1, -3)
        self.assertEqual(-4, res3)


#  使用unittest 框架进行测试的同时，有大量的重复代码，所以我们需要测试数据和测试代码分离，优化代码


cases = [{"params1": 1, "params2": 2, "exp": 3},
         {"params1": 10, "params2": 20, "exp": 30},
         {"params1": -1, "params2": -2, "exp": -3},
         {"params1": 1, "params2": -2, "exp": -1},
         {"params1": -11, "params2": -22, "exp": -333},
         {"params1": 15, "params2": 25, "exp": 40}]


@ddt
class TestAdd01(unittest.TestCase):
    @data(*cases)  # 代表该方法循环使用cases中的数据，cases有多少条，该方法执行多少条，该方法执行多少次，*代表拆包
    def test(self, case):  # 拆包后的数据会循环赋值给case，并且执行该方法
        res2 = add(case['params1'], case['params2'])
        self.assertEqual(case['exp'], res2)
