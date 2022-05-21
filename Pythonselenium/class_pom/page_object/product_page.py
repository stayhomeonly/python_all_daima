"""
#@Time：2022/5/18-16:41
#@file：product_page
#@Project:Pythonselenium
#@Content:

"""
from selenium.webdriver.common.by import By

from class_pom.base.base_page import BasePage

"""
商品详情页
"""
from selenium import webdriver

class ProductPage(BasePage):
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html'

    # 核心元素
    suite = (By.XPATH, '//li[@class="sku-line "]')
    colore = (By.XPATH, '//li[@class="sku-line  sku-line-images"]')
    memory = (By.XPATH, '//li[@data-value="32G"]')
    add = (By.XPATH, '//button[@title="加入购物车"]')

    # 业务流 添加购物车
    def addcart(self):
        self.open(self.url)
        self.click(self.suite)
        self.sleep(1)
        self.click(self.colore)
        self.sleep(1)
        self.click(self.memory)
        self.sleep(1)
        self.click(self.add)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    ProductPage(driver).addcart()



