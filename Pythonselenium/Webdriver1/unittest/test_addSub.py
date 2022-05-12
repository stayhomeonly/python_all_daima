'''
---------------------------
File Name:test_addSub
Author:FENGXIN
date:2022/3/21-14:15

---------------------------

'''
from Webdriver1.unittest.calculator import *
import unittest


class Test_add(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = Math(5, 5)
        self.assertEqual(j.add(), 10)

    def test_add1(self):
        j = Math(10, 20)
        self.assertEqual(j.add(), 30)


class Test_sub(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_sub1(self):
        i = Math(6, 2)
        self.assertEqual(i.sub(), 4)

    def tearDown(self):
        print("test end")

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    suite = unittest.TestSuite
    suite.addTest("test_add")
    suite.addTest("test_add1")
    # suite.addTest("test_sub1")

    runer = unittest.TextTestRunner()
    runer.run()
