'''
---------------------------
File Name:base_page
Author:FENGXIN
date:2022/3/21-16:48

---------------------------

'''
'''
提供基础的函数，给所有的页面对象执行：
    元素定位
    切换页面
    访问url
    输入
    点击
    
'''

from selenium import webdriver


class BasePage:
    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问URL
    def open(self, url):
        self.driver.get(url)

    # 退出
    def quit(self):
        self.driver.quit()

    # 元素定位
    def loctor(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.loctor(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.loctor(loc).click()
