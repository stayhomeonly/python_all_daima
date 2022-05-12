'''
---------------------------
File Name:case
Author:FENGXIN
date:2022/4/10-11:20

---------------------------

'''
import unittest
from time import sleep

from selenium import webdriver
from ddt import ddt, file_data

from Webdriver1.Pom_class.page_object.login_page import LoginPage
from Webdriver1.Pom_class.page_object.product_page import ProductPage


@ddt
class Case(unittest.TestCase):
    # def setUp(self):  # 如果用这种每次运行都会打开和关闭，driver就没有办法共用
    #     self.driver = webdriver.Chrome()
    #
    #     self.lp = LoginPage(self.driver)
    #     self.pp = ProductPage(self.driver)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.pp = ProductPage(cls.driver)  # 写这个代表两个方法调用的是一个driver

    # def tearDown(self):
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data('../data/login.yaml')
    def test_01_login(self, usr, pwd):
        self.lp.login(usr, pwd)

    def test_02_product(self):
        self.pp.addcart()
        sleep(3)


if __name__ == '__main__':
    unittest.main()
