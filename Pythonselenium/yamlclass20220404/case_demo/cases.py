'''
---------------------------
File Name:test_cases
Author:FENGXIN
date:2022/4/4-17:38

---------------------------

'''
import unittest

from ddt import ddt, file_data
from selenium import webdriver


@ddt
class CaseDemo(unittest.TestCase):
    # @file_data('../data/data4.yaml')
    # def test_01(self, **kwargs):  # 如果要传递字典类型的内容，通过**kwargs形式传送
    #     # driver = webdriver.Chrome()
    #     # driver.get(kwargs['url'])
    #     # driver.find_element_by_id('kw').send_keys(kwargs['txt'])
    #     print(kwargs['url'])
    #     print(kwargs['params'])

    @file_data('../data/login.yaml')
    def test_02(self, **kwargs):  # 如果要传递字典类型的内容，通过**kwargs形式传送
        # driver = webdriver.Chrome()
        # driver.get(kwargs['url'])
        # driver.find_element_by_id('kw').send_keys(kwargs['txt'])
        print(kwargs)
        print(kwargs['username'])
        print(kwargs['passwd'])


if __name__ == '__main__':
    unittest.main()
