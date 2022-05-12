'''
---------------------------
File Name:Ftest_api.py
Author:FENGXIN
date:2022/1/20-21:12

---------------------------

'''
import pytest


#
# @pytest.fixture(scope='function')
# def test_fixture():
#     print('部分前置')
#
#     yield
#     print('部分后置')


# 如果想给类使用部分前置和后置，用的是@pytest.mark.usefixtures(test_fixture)括号里面是方法名

class TestApi:

    # def setup(self):
    #     print('用例之前执行')
    #
    # def teardown(self):
    #     print('用例之后执行')
    #
    # def setup_class(self):
    #     print('-----每个测试类之前执行')
    #
    # def teardown_class(self):
    #     print('--------每个测试类之后执行')

    def test_mashang(self):
        print('马上教育')

    def test_001(self,test_fixture):
        assert 5 > 4

    def test_002(self):
        print('天下第一剑')
