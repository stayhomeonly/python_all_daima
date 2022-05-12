"""
#@Time：2022/5/1-15:43
#@file：screen_shot
#@Project:python_basic05.py
#@Content:

"""
# 截图
from Appium1.find_element.capability import driver
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('fengxin1')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('FENG12345')

driver.save_screenshot('login.png')
driver.get_screenshot_as_file('./images/login.png')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()