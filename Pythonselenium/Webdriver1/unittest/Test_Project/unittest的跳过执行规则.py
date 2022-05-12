'''
---------------------------
File Name:unittest的跳过执行规则
Author:FENGXIN
date:2022/3/25-20:44

---------------------------

'''
'''
•	unittest.skip() 直接跳过测试
•	unittest.skipIf() 条件为真，跳过测试
•	unittest.skipUnless 条件为假，跳过测试
•	unittest.expectedFailure 预期设置失败

'''
import unittest


class Test1(unittest.TestCase):

    def setUp(self):
        print("Test1 start")

    @unittest.skipIf(4 > 3, "skip Test_d")
    def test_c(self):
        print("test_c")

    # @unittest.skipUnless(1<0, "skip test_b")
    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("Test1 end")


@unittest.skip(" skip Test_2")
class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")

    def test_d(self):
        print("test_d")

    # @unittest.expectedFailure
    def test_a(self):
        print("test_a")

    def tearDown(self):
        print("Test2 end!")


if __name__ == '__main__':
    unittest.main()
