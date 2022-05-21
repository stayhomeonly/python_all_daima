"""
#@Time：2022/5/15-13:49
#@file：comm_fun
#@Project:python_basic05.py
#@Content:

"""
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# 封装通用公共类 common_fun.py
from Appium1.kyb_testProject.baseView.base_view import BaseView
from Appium1.kyb_testProject.common.desired_caps import appium_desired


class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    wemedia_canel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_cancelBtn(self):
        logging.info("============check_cancelBtn===============")

        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('update element is not found!')
        else:
            logging.info('click cancelBtn')
            element.click()

    def check_skipBtn(self):
        logging.info("==========check_skipBtn===========")
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skipBtn element is not found!')
        else:
            logging.info('click skipBtn')
            element.click()

    # 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[0] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)
    # 对于登录之后弹窗进行处理，如果有就点击关闭，如果没有不影响
    def check_market_ad(self):
        logging.info('=====check_market_ad=======')
        try:
            element = self.driver.find_element(*self.wemedia_canel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    # com.check_skipBtn()
    com.swipeLeft()
    com.getScreenShot("startApp")
