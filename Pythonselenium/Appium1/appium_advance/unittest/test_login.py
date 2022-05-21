"""
#@Time：2022/5/16-16:56
#@file：test_login
#@Project:Pythonselenium
#@Content:

"""
import logging
import unittest

from Appium1.appium_advance.page_object.loginView import LoginView
from Appium1.appium_advance.unittest.myunit import Startup


class TestLogin(Startup):
    def test_login_zxw2018(self):
        logging.info('=======test_login_zxw2018=========')
        l = LoginView(self.driver)
        l.login_action('fengxin1', 'FENG1234')


if __name__ == '__main__':
    unittest.main()
