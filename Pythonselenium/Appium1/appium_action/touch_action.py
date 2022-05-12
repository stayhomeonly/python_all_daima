"""
#@Time：2022/5/5-15:36
#@file：touch_action
#@Project:python_basic05.py
#@Content:

"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'

desired_caps['app'] = r'C:\Users\Shuqing\Desktop\mymoney.apk'
desired_caps['appPackage'] = 'com.mymoney'
desired_caps['appActivity'] = 'com.mymoney.biz.splash.SplashScreenActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def swipeLeft():
    l = get_size()
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)


# 等待启动页面元素，然后向左滑动两次,跳过引导页面
WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id("com.mymoney:id/next_btn"))
for i in range(2):
    swipeLeft()
    sleep(1)

# 点击“开始随手记”按钮
driver.find_element_by_id('com.mymoney:id/begin_btn').click()

# 检测是否有活动页面弹窗，如果有就点击关闭
try:
    closBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closBtn.click()

# 点击更多菜单
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()

# 等待界面菜单加载出来，然后向上滑动
WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id("com.mymoney:id/content_container_ly"))
swipeUp()

# 点击高级菜单
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
# 点击密码与手势密码菜单
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
# 点击手势密码保护
driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

# 连续滑动两次设置图案密码
for i in range(2):
    TouchAction(driver).press(x=243, y=381).wait(2000) \
        .move_to(x=455, y=390).wait(1000) \
        .move_to(x=643, y=584).wait(1000) \
        .move_to(x=647, y=784).wait(1000) \
        .release().perform()
