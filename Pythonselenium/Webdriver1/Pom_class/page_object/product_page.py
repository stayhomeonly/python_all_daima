'''
---------------------------
File Name:product_page
Author:FENGXIN
date:2022/4/10-10:53

---------------------------

'''
from Webdriver1.Pom_class.base.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # 页面的url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html'
    # 页面关联的核心元素
    suite = (By.XPATH, '//li[@data-value="套餐一"]')  # 套件
    color = (By.XPATH, '//li[@data-value="金色"]')  # 颜色
    memory = (By.XPATH, '//li[@data-value="128G"]')  # 容量
    cart = (By.XPATH, '//button[@title="加入购物车"]')  # 加入购物车

    # 页面关联的业务
    def addcart(self):
        self.open(self.url)

        self.click(self.suite)
        sleep(1)
        self.click(self.color)
        sleep(1)
        self.click(self.memory)
        sleep(1)
        self.click(self.cart)
