# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
=============================
"""
# 1、pytest 安装
# pip install -U pytest
# >pytest --version 查看 pytest版本
'''
标记:
默认情况下，pytest 会递归查找当前目录下所有以 test 开始或结尾的 Python 脚本，
并执行文件内的所有以 test 开始或结束的函数和方法。
'''

import pytest


class TestClass:
    @pytest.mark.skip()
    def test_one(self):
        x = "this"
        assert 'h' in x

    # 如果你事先知道测试函数会执行失败，但又不想直接跳过，而是希望显示的提示，可以使用pytest.mark.xfail()
    @pytest.mark.xfail()
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    pytest.main(['-s', './test_py_02.py'])  # 运行指定模块


class Test_mark():
    @pytest.mark.test01
    def test_a(self):
        print("mark test a")

    @pytest.mark.test02
    def test_b(self):
        print("mark test b")


if __name__ == '__main__':
    pytest.main(['-s', "pytest6.py"])

# pytest -m test01
# pytest -n "test01 or test02"
# pytest -m "not test01"
