'''
---------------------------
File Name:testorder
Author:FENGXIN
date:2022/3/21-16:17

---------------------------

'''
import unittest


# 执行顺序规则——测试类或测试方法的数字与字母顺序 0~9，A-Z


class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1 start")

    def test_c(self):
        print("test_c")

    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("test end")


class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")

    def test_d(self):
        print("test_d")

    def test_a(self):
        print("test_a")

    def tearDown(self):
        print("Test2 end!")


if __name__ == '__main__':
    # unittest.main()

    suite= unittest.TestSuite()
    suite.addTest(Test2('test_d'))
    suite.addTest(Test2('test_a'))

    runner = unittest.TextTestRunner()
    runner.run(suite)   # 用cmd运行执行，则是按照自己添加的顺序来执行
