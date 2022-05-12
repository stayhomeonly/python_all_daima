'''
---------------------------
File Name:test_Math
Author:FENGXIN
date:2022/3/18-21:00

---------------------------

'''
from Webdriver1.unittest.calculator import Math
import unittest


class TestMath(unittest.TestCase):
    def setUp(self):
        print("Start test")

    def test_add(self):
        j = Math(5, 10)
        self.assertEqual(j.add(), 15)
        # 用例失败场景
        # self.assertEqual(j.add(), 12)

    def test_add1(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 12)

    def test_assertTrue(self):
        j = Math(5, 10)
        self.assertTrue(j.add() > 10)

    def test_assertIn(self):
        a = '51zxw'
        b = 'hello 51zxw'
        self.assertIn(a, b)

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestMath("test_add"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()
