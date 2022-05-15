"""
#@Time：2022/5/15-13:49
#@file：comm_fun
#@Project:python_basic05.py
#@Content:

"""
# 封装通用公共类 common_fun.py
from Appium1.appium_advance.page_object.base_view  import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from Appium1.appium_advance.page_object.desired_caps import appium_desired

class Common(BaseView):

    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')

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

if __name__ == '__main__':

    driver=appium_desired()
    com=Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()
