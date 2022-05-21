"""
#@Time：2022/5/16-16:23
#@file：loginView
#@Project:Pythonselenium
#@Content:

"""
import logging
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Appium1.kyb_testProject.common.comm_fun import Common
from Appium1.kyb_testProject.common.desired_caps import appium_desired


class LoginView(Common):
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')

    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    RightButton = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # 设置键
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    def login_action(self, username, password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("========================login_action===========")

        logging.info("usename is :%s" % username)
        sleep(2)  # 加这个就是为了防止有些时候定位不到，也可以不加
        self.find_element(*self.username_type).send_keys(username)
        logging.info("usename is :%s" % username)

        logging.info("password is :%s" % password)
        self.find_element(*self.password_type).send_keys(password)

        logging.info("click loginBtn")
        self.driver.find_element(*self.loginBtn).click()

        logging.info("login finished")

    # 处理登录账号没有退出，显示窗口
    def check_account_alert(self):
        logging.info("======check_account_alert=====")
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip_commit')
            element.clixk()

    def logout_action(self):
        logging.info('===logout_action=====')
        self.driver.find_element(*self.RightButton).click()
        sleep(3)
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()

    def check_loginStatus(self):
        logging.info('======check_login_status======')
        self.check_market_ad()
        self.check_account_alert()
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login Fail')
            # self.getScreenShot('login fail')  # 截图
            return False

        else:
            logging.info('login success')
            self.logout_action()
            return True


def check_loginStatus(self):
    logging.info('======check_login_status======')
    self.check_market_ad()
    self.check_account_alert()
    try:
        self.driver.find_element(*self.button_mysefl).click()
        self.driver.find_element(*self.username)
    except NoSuchElementException:
        logging.error('login Fail')
        # self.getScreenShot('login fail')  # 截图
        return False

    else:
        logging.info('login success')
        self.logout_action()
        return True


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('fengxin1', 'FENG1234')
    l.check_loginStatus()
