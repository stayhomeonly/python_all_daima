'''
---------------------------
File Name:Open_51zxwBaidu
Author:FENGXIN
date:2022/3/5-10:36

---------------------------

'''
from selenium import webdriver

from time import sleep

# 加载浏览器驱动
driver = webdriver.Firefox()


# 打开自学网页面
driver.get("http://www.51zxw.net")
print(driver.title)
sleep(3)

# 打开百度页面
driver.get("http://www.baidu.com")
print(driver.title)
sleep(2)

# 退出浏览器
driver.quit()
