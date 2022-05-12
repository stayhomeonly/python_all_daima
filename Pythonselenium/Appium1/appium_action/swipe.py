"""
#@Time：2022/5/4-16:41
#@file：swipe
#@Project:python_basic05.py
#@Content:

"""
from time import sleep

from Appium1.find_element.capability import driver


# 获取屏幕尺寸
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


l = get_size()
print(l)  # 一直显示'WebDriver' object has no attribute 'w3c'报错


def swipeLeft():
    l = get_size()
    x1 = int(l[0] * 0.9)
    y1 = int(l[0] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


for i in range(2):
    swipeLeft()
    sleep(0.5)

driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()
