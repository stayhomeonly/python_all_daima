"""
#@Time：2022/5/3-18:07
#@file：test_cases
#@Project:python_basic05.py
#@Content:

"""
'''
1、pytest默认规则是读取所有以test开头的文件夹和子文件。
2、pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
3、如果想单独运行一个案例  pytest -vs test_cases.py::test_01
# 进入单独一个文件，在运行单独一个函数
'''
import pytest


# 测试用例
def test_02():
    print('test_02')


def test_01():
    print('test_01')


# pytest 运行主入口
if __name__ == '__main__':
    pytest.main(['-vs'])
