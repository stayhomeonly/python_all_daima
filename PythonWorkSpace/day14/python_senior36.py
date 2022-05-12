"""
=========================
File Name:python_senior36
Author:冯鑫
Date:2021/12/4-11:41
==========================
"""
import unittest

'''
测试夹具
'''


class TestFixture(unittest.TestCase):
    # def setUp(self):  # 每条用例执行前执行
    #     print("每条用例执行前执行")
    #
    # def tearDown(self):  # 每条用例执行后执行
    #     print('每条用例执行之后执行!')

    @classmethod
    def setUpClass(cls):
        print('每个测试类执行之前执行')

    @classmethod
    def tearDownClass(cls):
        print("每个测试类执行之后执行")

    def test01(self):
        print('这是测试用例case1')

    def test02(self):
        print("这是测试用例case2")
