"""
#@Time：2022/5/16-20:20
#@file：base_page
#@Project:Pythonselenium
#@Content:

"""
from time import sleep

"""
基类，提供所有的常用函数，进行二次封装，便于页面对象的调用
"""
from selenium import webdriver


class BasePage:

    # 提供一个构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def loctor(self, loc):  # loc元组
        return self.driver.find_element(*loc)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 输入
    def input(self, loc, txt):
        self.loctor(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.loctor(loc).click()

    # 等待
    def sleep(self, time_):
        sleep(time_)
    #


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = "http://www.baidu.com"
    BasePage(driver).open(url)
