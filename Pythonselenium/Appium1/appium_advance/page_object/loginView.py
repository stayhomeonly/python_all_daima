"""
#@Time：2022/5/16-16:23
#@file：loginView
#@Project:Pythonselenium
#@Content:

"""
import logging

from selenium.webdriver.common.by import By

from Appium1.appium_advance.page_object.comm_fun import Common
from Appium1.appium_advance.page_object.desired_caps import appium_desired
class LoginView(Common):
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')

    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("========================login_action===========")

        logging.info("usename is :%s" %username)
        self.find_element(*self.username_type).send_keys(username)
        logging.info("usename is :%s" % username)

        logging.info("password is :%s"%password)
        self.find_element(* self.password_type).send_keys(password)

        logging.info("click loginBtn")
        self.driver.find_element(*self.loginBtn).click()

        logging.info("login finished")

if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('fengxin1','FENG1234')