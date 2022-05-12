'''
---------------------------
File Name:By_tagname
Author:FENGXIN
date:2022/3/5-14:31

---------------------------

'''
from selenium import webdriver
from time import sleep

# tag_name定位
# 案例：打开我要自学网页面，在用户名输入框输入用户名“selenium”


# 加载浏览器
driver = webdriver.Firefox()

driver.get("http://www.51zxw.net")
# 定位标签名为input的元素
# driver.find_element_by_tag_name("input").send_keys("Selenium")


# 获取页面所有标签名称为“input”的标签。
driver.find_elements_by_tag_name("input")[0].send_keys("selenium")
sleep(3)
driver.quit()
