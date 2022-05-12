'''
---------------------------
File Name:By_css_selector
Author:FENGXIN
date:2022/3/6-21:15

---------------------------

'''
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

# driver.get("http://www.baidu.com")
# 根据id来定位,#id id选择器根据id属性来定位元素
# driver.find_element_by_css_selector("#kw").send_keys('Selenium 我要自学网')
# sleep(2)
# driver.find_element_by_id("su").click()
# sleep(2)
# driver.quit()

# 通过class定位	.class  class选择器，根据class属性值来定位元素
# driver.find_element_by_css_selector(".s_ipt").send_keys("Selenium")
# sleep(2)
# driver.find_element_by_id("su").click()
# sleep(2)


# 通过属性来定位.	[attribute='value'] 根据属性来定位元素
# driver.find_element_by_css_selector('[autocomplete="off"]').send_keys("Python")
# sleep(2)
# driver.find_element_by_id("su").click()
# sleep(2)


driver.get("http://www.51zxw.net")
sleep(3)
driver.find_element_by_xpath("//*[@class='user pos-r']").click()
sleep(3)
# 通过元素层级来定位
# driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("51zxw")
driver.find_element_by_css_selector("#loginStr").send_keys("51zxw")
sleep(2)
driver.quit()
