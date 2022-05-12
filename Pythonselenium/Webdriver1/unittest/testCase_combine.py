'''
---------------------------
File Name:testCase_combine
Author:FENGXIN
date:2022/3/21-16:01

---------------------------

'''
from Webdriver1.unittest.calculator import *
import unittest


class Test_StarEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")


class Testadd(Test_StarEnd):
    def test_add(self):
        j = Math(5, 5)
        self.assertEqual(j.add(), 10)


class TestSub(Test_StarEnd):
    def test_sub(self):
        i = Math(3, 2)
        self.assertEqual(i.sub(), 1)


if __name__ == '__main__':
    unittest.main()
