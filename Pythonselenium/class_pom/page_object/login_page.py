"""
#@Time：2022/5/17-20:19
#@file：login_bage
#@Project:python_basic05.py
#@Content:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
登录页面对象，用于系统的登录操作
'''
from class_pom.base.base_page import BasePage


class LoginPage(BasePage):
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 核心元素
    user = (By.XPATH, '//input[@name="accounts"]')
    password = (By.XPATH, '//input[@name="pwd"]')
    button = (By.XPATH, '//button[text()="登录"]')

    # 业务流
    def login(self, usr, pwd):
        self.open(self.url)
        self.input(self.user, usr)
        self.input(self.password, pwd)
        self.click(self.button)
        self.sleep(3)



if __name__ == '__main__':
    driver = webdriver.Chrome()
    usr='xuzhu666'
    pwd='123456'
    LoginPage(driver).login(usr, pwd)
