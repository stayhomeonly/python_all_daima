'''
---------------------------
File Name:demo_2
Author:FENGXIN
date:2022/4/2-13:32

---------------------------

'''
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 设置隐形等待，纯粹基于webdriver来进行调用的，只用执行一次，就可以用于全局
# 设置一个隐形的等待，设置最长的等待时间，如果在这个时间内完成了页面的内容全部加载，则进行下一步
# ，否则一直等待时间结束，再进行下一步
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

driver.find_element_by_xpath('//input[@id="kw"]').send_keys("虚竹")
driver.find_element_by_xpath('//input[@id="su"]').click()
# 强制等待，必须要操作，无所谓的阶段
# sleep(5)

# driver.find_element_by_xpath('//a[@aria-label="虚竹，武侠小说《天龙八部》中的男主角之一，百度百科"]').click()

# 显示等待
# 专门用于指定的条件进行等待,再设置的最大时长内，依照查找的时间频率来进行搜索，查找指定的对象，until
# 表示如果找到，则继续下一步，否则，报出异常NoSuchElementException;Until_Not()与Until相反
# 有点：精确对某个特定条件进行等待，不会浪费多余的任何时间再等待上。如果条件成立，立即进入下一步，如果不成立
# 则抛出异常

# 设置显示等待
# 通过写法
WebDriverWait(driver, 20, 0.5).until(lambda el: driver.find_element_by_xpath('//a[@class="no-outline-while-click"]'))
driver.find_element_by_xpath('//a[@class="no-outline-while-click"]').click()

# 其他写法
locator = (By.XPATH, '//a[@class="no-outline-while-click"]')
WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located(locator))
driver.find_element_by_xpath('//a[@class="no-outline-while-click"]').click()
