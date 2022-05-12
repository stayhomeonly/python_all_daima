'''
---------------------------
File Name:By_xpth2_P2
Author:FENGXIN
date:2022/3/5-21:24

---------------------------

'''
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.51zxw.net")

driver.find_element_by_xpath("//*[@class='user pos-r']").click()
sleep(3)

# driver.find_element_by_xpath("//input[@id='loginStr']").send_keys("15161039042")

# 逻辑运算组合定位
driver.find_element_by_xpath("//input[@class='input-text size-L radius icon' and @name='loginStr']") \
    .send_keys("15161039042")
sleep(3)

driver.find_element_by_xpath("//input[@id='pwd']").send_keys("FENG1234")
sleep(3)

driver.find_element_by_xpath("//*[@class='btn radius size-L btn-danger']").click()
sleep(3)
# 如果当前元素都是重复，或者属性都是重复，要用层层递进的方式寻找列如：
# 层级和属性结合定位--自学网首页输入用户和名密码
# driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys("51zxw")

driver.quit()
