"""
#@Time：2022/4/30-17:16
#@file：get_toast
#@Project:python_basic05.py
#@Content:

"""
from selenium.webdriver.support.ui import WebDriverWait

# coding=utf-8
from Appium1.find_element.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('fengxin1')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('FENG12345')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

# 用户名和密码错误
error_message = "用户名或者密码错误，你还可以尝试2次"
limit_message = "验证失败过多，请15分钟过后再试"

message = '//*[@text=\'{}\']'.format(error_message)
# message='//*[@text=\'{}\']'.format(limit_message)

# message = '//*[@text="用户名或者密码错误，你还可以尝试3次"]'

toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
print(toast_element.text)
# 一直显示超时
