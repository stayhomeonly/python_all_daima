"""
#@Time：2022/4/30-10:43
#@file：element_wait
#@Project:python_basic05.py
#@Content:

"""
'''
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver : WebDriver
timeout : 最长超时时间，默认以秒为单位
poll_frequency : 休眠时间的间隔时间，默认为0.5秒
ignored_exceptions : 超时后的异常信息，默认情况下抛NoSuchElementException异常。

'''
from selenium.webdriver.support.ui import WebDriverWait

from Appium1.find_element.kyb_login import driver

WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'))

driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
