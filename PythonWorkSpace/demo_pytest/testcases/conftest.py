'''
---------------------------
File Name:Fconftest.py
Author:FENGXIN
date:2022/1/18-20:03

---------------------------

'''
'''
conftest.py文件：
配置里可以实现数据共享，不需要import就能自动找到一些配置。
conftest文件实际应用需要结合fixture来使用，fixture中参数scope也适用conftest中fixture的特性
'''

import pytest


#
# @pytest.fixture(scope='session', autouse=True)
# def test():
#     print('conftest...,链接数据库%')
#
#     yield
#
#     print('conftest...,关闭数据库')

@pytest.fixture(scope='class')  # 如果想在类加部分前置和部分后置，用装饰器，@pytest.fixture(scope='class')
# 如果想在方法用部分前置和后置，直接定义的方法名加在self中
def test_fixture():
    print('部分前置')

    yield
    print('部分后置')
