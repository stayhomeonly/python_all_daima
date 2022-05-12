# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
固件（Fixture）是一些函数，pytest 会在执行测试函数之前（或之后）加载运行它们。

# function: 函数级，每个测试函数都会执行一次固件；
# class: 类级别，每个测试类执行一次，所有方法都可以使用；
# module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
# session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。
=============================
"""

import pytest


# 方式1：在测试函数里通过参数，指定要使用的测试固件。
# # 案例1：
# @pytest.fixture()  # 每个测试方法之前运行
# def data():
#     print(1234)
#
# def test_pass1(data):# 测试成功
#     pass
# def test_pass2(data):
#     pass


#  案例2：
# @pytest.fixture()
# def db():
#     print('opened')
#     yield
#     print('closed')
#
#
# def test_pass1(db):
#     pass
# def test_pass2(db):
#     pass
# #

# 案例
# @pytest.fixture()  # fixture标记的函数可以应用于测试类外部
# def bf():
#         print('opened')
#         yield
#         print('closed')
#
# @pytest.mark.usefixtures("bf")
# class Test_ABC:
#     def setup(self):
#         print("------->A")
#
#     def test_a(self):
#         print("------->B")
#         assert 1
#
#


# 方式2：
# 将测试固件装饰器pytest.fixture的参数autouse设为True，测试函数会自动使用该测试固件。

@pytest.fixture(scope='function', autouse=True)  # 在当前模块每个测试方法之前自动执行
def func_scope():
    print('--function--')


@pytest.fixture(scope='module', autouse=True)  # 在当前模块  之前自动执行
def mod_scope():
    print('--module--')


#
@pytest.fixture(scope='session', autouse=True)  # 从执行效果来看，这个只在当前模块运行
def sess_scope():
    print('--session--')


@pytest.fixture(scope='class', autouse=True)  #
def class_scope():
    print('--class--')


def test_pass1():
    print('AAAA')


def test_pass2():
    print('BBBB')


#
# # 方式3
# @pytest.fixture(name="lg")
# def login():
#     print('登录系统')
#
#
# @pytest.mark.usefixtures("lg")
# def test_1():
#     print(1234)

if __name__ == '__main__':
    pytest.main(['-v', '-s', './test_py_04.py'])

# 方式4:
# python会自动加载当前模块的conftest.py文件里的自定义测试固件，一般可以在根目录里定义更通用的自定义测试固件
# 注意注意conftest.py文件名是系统规定的名字
