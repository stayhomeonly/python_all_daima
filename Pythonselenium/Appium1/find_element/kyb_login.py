'''
---------------------------
File Name:kyb_login
Author:FENGXIN
date:2022/4/22-17:12

---------------------------

'''
from Appium1.find_element.capability import driver, NoSuchElementException

# 登录方法
def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('fengxin1')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('FENG1234')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()

    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
    login()
