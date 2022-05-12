'''
---------------------------
File Name:loginpage
Author:FENGXIN
date:2022/3/21-17:13

---------------------------

'''
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
登录页面对象，用于封装登录页要进行的所有操作行为
    
'''
from Webdriver1.Pom_class.base.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # 页面的url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 页面关联的核心元素:基于定位方法+定位值进行元素的定位
    username = (By.XPATH, '//input[@name="accounts"]')
    password = (By.XPATH, '//input[@name="pwd"]')
    button = (By.XPATH, '//button[text()="登录"]')

    # 页面关联的业务
    def login(self, usr, pwd):
        self.open(self.url)
        self.input(self.username, usr)
        self.input(self.password, pwd)
        self.click(self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    usr = 'xuzhu666'
    pwd = '123456'
    lp.login(usr, pwd)
