"""
#@Time：2022/5/6-14:35
#@file：multi_action
#@Project:Pythonselenium
#@Content:

"""
from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['platforVersion'] = '7.1.2'

desired_caps['app'] = r'C:\Users\Shuqing\Desktop\com.baidu.BaiduMap.apk'  # 改一下
desired_caps['appPackage'] = 'com.baidu.BaiduMap'
desired_caps['appActivity'] = 'com.baidu.baidumaps.WelcomeScreen'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()

x = driver.get_window_size()['width']  # 一直没法定位
y = driver.get_window_size()['height']


def pinch():  # 缩写
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
    action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()

    print('start pinch...')
    zoom_action.add(action1, action2)
    zoom_action.perform()


def zoom():  # 放大
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    print('start zoom...')
    zoom_action.add(action1, action2)
    zoom_action.perform()


if __name__ == '__main__':
    for i in range(3):
        pinch()

    for i in range(3):
        zoom()
