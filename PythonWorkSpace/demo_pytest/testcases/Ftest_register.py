'''
---------------------------
File Name:testregister
Author:FENGXIN
date:2022/1/15-10:14

---------------------------

'''
"""
单独执行某个py文件中的所有用例
pytest test.py
执行目录下所有用例	
pytest testcase/
单独执行某个用例
以函数形式的用例
pytest Ftest_login.py::test_1
以类形式的用例
pytest Ftest_login.py::TestClass::test_1
"""
import pytest


# def test_login():
#     print("登录测试  函数")
#     assert 5 == 4
#
#
def test_01():
    print("注册测试  函数")


class TestRegister:
    def test_login(self):
        print("登录测试  函数")

    @pytest.mark.age
    def test_register1(self):
        print("age  函数")

# 如果我只想运行某个文件中的某个函数 pytest Ftest_register.py::test_01 -s
# _代表进入test_register.py下面的test_01的函数，”::“代表进入某个模块的指定方法

# 如果想进入某个类里面的方法：pytest Ftest_register.py::TestRegister::test_login -s

# -s：显示详细日志信息
# -v：更加详细结果信息
# --html=report.html：生成测试报告  pytest --html =..\reports\report.html
# -n NUM：多进程运行
# -m：运行执行标记的测试用例
# -k：关键字参数，执行带关键的测试用例
# -q：显示测试结果信息
