"""
=========================
File Name:assert_33
Author:冯鑫
Date:2021/12/3-17:35
==========================
"""
import unittest


class Test(unittest.TestCase):
    def test01(self):
        a = b = 1
        self.assertEqual(a, b)  # 断言a 和b相等

    def test02(self):
        list1 = [1, 2, 3]
        self.assertIn(2, list1)  # 断言2是否在list1中

    def test03(self):
        self.assertTrue(1 > 0)  # 断言（）中是否为真

    def test04(self):
        self.assertIsNone(None)  # 断言()中是否为空

    # 案例
    def test05(self):
        dict1 = {'code': 1000, "msg": "登录成功",
                 "token": "MTYzODU1NDU3OS40NTUyOTMyOjY3NjIzMDM0YTcxNjBiZTM5NDA0MDcyNjFiOTA3ZWU3NGJkMmZiZTM="}
        self.assertIn('登录成功', dict1["msg"], msg='断言错误，响应报文没有返回登录成功')
