"""
#@Time：2022/4/29-16:53
#@file：by_Uiautomator
#@Project:python_basic05.py
#@Content:

"""
from appium.webdriver.common.appiumby import AppiumBy

from Appium1.find_element.capability import driver
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').clear()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').\
#     send_keys('fengxin1')

# driver.find_element_by_android_uiautomator('new UiSelector().text("请输入用户名")').send_keys('fengxin1')

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText")').send_keys('fengxin1')

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').\
    send_keys('FENG1234')

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()