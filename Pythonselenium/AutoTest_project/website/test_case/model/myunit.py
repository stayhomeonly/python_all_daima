'''
---------------------------
File Name:myunit
Author:FENGXIN
date:2022/3/30-19:45

---------------------------

'''
import unittest

from AutoTest_project.driver.driver import *


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) :
        self.driver.quit()