"""
#@Time：2022/5/3-18:07
#@file：test_cases
#@Project:python_basic05.py
#@Content:

"""
'''
1、pytest默认规则是读取所有以test开头的文件夹和文件。
2、pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
3、多条指令一同运行时，需要通过空格进行区分，在main函数中，是通过逗号进行分割
4、-rA用于测试结果简单统计
5、pytest中的setup和teardown：一般可以通过一个配置文件直接进行配置进行管理：
配置文件命令一定是conftest.py
fixture
'''
import pytest


# 前置条件和后置条件
def setup_function():
    print('function')


def teardown_function():
    print('tfunction')


# 测试用例
def test_02():
    print('test_02')


def test_01():
    print('test_01')


# pytest中class对象的定义：建议以test开头
'''
在class中前置后置函数的运行顺序等级：
    setup class
    setup method
    setup
    teardown
    teardown method
    teardown class
    
'''


class TestDemo:
    def test_d1(self):
        print('testd1')

    def test_d2(self):
        print('testd2')


# pytest 运行主入口
if __name__ == '__main__':
    pytest.main(['-vs', '-rA'])
