"""
--------------------------------
@Time  : 2022/2/24-------19:33
@author  :  ztt
@File  :  python_basic02 
--------------------------------
"""
"""
测试固件(测试夹具)
使用固件的三种方式
1,@pytest.fixture(autouse=True):声明固件时会设置autouse=True会自动使用固件
2,在需要使用固件的case参数传入固件函数名即可
3,使用pytest.mark.usefixture('固件名')装饰器装饰需要使用固件地的case
4,固定配置文件,python会自动加载当前目录下的conftest.py文件,一般可以根据目录里定义的通用的自定义固件
注意:conftest.py和pytest.ini文件都是系统规定的名字
5,autouse=True是指该固件每个test都调用一遍
"""
import pytest


# 在当前模块使用固件，夹具
class TestFixture:
    @pytest.mark.usefixtures("class_scope")  # 引用conftest的固件
    def test_01(self):
        print('开始执行case01--')

    def test_02(self):
        print('开始执行case02--')


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest_05.py'])
