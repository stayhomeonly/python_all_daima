"""
#@Time：2022/5/4-18:31
#@file：conftest.py
#@Project:python_basic05.py
#@Content:

"""
'''
这是pytest中的setup和teardown的配置文件:注意，文件名称一定是conftest，不能是其他
scope参数定义的4种等级(默认等级是function)
    session:在本次session级别中只执行一次
    moudle:模块级别中只执行一次
    class:在类执行中只执行一次
    function：在函数级别中执行一次，每有一个函数就执行一次

'''
import pytest


# 预置函数：用于前期的数据准备
@pytest.fixture(scope='function')
def xuzhu():
    print('虚竹生病了，但是很强')


@pytest.fixture()
def xuzhu01():
    return 1
