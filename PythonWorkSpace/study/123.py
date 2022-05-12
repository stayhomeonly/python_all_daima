'''
---------------------------
File Name:123
Author:FENGXIN
date:2022/4/19-21:38

---------------------------

'''
import unittest

from ddt import ddt, data, unpack
from selenium import webdriver

from time import sleep


@ddt
class TestLogin(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
        self.driver.implicitly_wait(100)

    def tearDown(self) -> None:
        self.driver.quit()

    @data(['xuzhu666', '123456'],['123456','123456'])
    @unpack  # 参数数据，然后分别赋值给username,pwd,在一定要用@unpack，不然无法单独分别赋值
    def test_1(self, username, pwd):
        self.driver.find_element_by_xpath('//input[@name="accounts"]').send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name="pwd"]').send_keys(pwd)
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()
        sleep(5)


if __name__ == '__main__':
    unittest.main()
