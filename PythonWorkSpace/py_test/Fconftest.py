# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-21:28
=============================
"""
# Fconftest.py
import pytest


#
# @pytest.fixture(scope='function', autouse=True)
# def func_scope():
#     print('-1-function-1-')
#
# @pytest.fixture(scope='module', autouse=True)
# def mod_scope():
#     print('-1-module-1-')
#
#
# @pytest.fixture(scope='session', autouse=True)
# def sess_scope():
#     print('-1-session-1-')


# @pytest.fixture(scope='class', autouse=True)  # 自动化方案2
# def class_scope():
#     print('-1-class-1-')


@pytest.fixture(scope='class')  # 想要在类加前置和后置，加装饰器@pytest.fixture(scope='class')，
# 如果只想方法前置和后置，直接写在self后面加函数名
def test_fixture():
    print('部分前置')
    yield
    print('部分后置')
