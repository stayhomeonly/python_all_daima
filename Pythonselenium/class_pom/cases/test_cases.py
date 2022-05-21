"""
#@Time：2022/5/17-20:47
#@file：test_cases
#@Project:python_basic05.py
#@Content:

"""
import unittest

from ddt import ddt, file_data
from selenium import webdriver

from class_pom.page_object.login_page import LoginPage
from class_pom.page_object.product_page import ProductPage


@ddt
class TestDemo(unittest.TestCase):
    # 类的初始化,为了不让每一次登录重新打开浏览器操作的
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.pp=ProductPage(cls.driver) # 这里为什么要见两个driver就是保证不会打开两个浏览器，是在同一页面

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 用例1
    @file_data('../data/user.yaml')
    def test_01_login(self, usr, pwd):
        self.lp.login(usr, pwd)

    def test_02_add(self):
        self.pp.addcart()


if __name__ == '__main__':
    unittest.main()
