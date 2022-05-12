'''
---------------------------
File Name:driver
Author:FENGXIN
date:2022/3/30-19:39

---------------------------

'''
from selenium import webdriver


# 定义浏览器
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()

    # driver.get("http://www.baidu.com")

    return driver


if __name__ == '__main__':
    browser()
