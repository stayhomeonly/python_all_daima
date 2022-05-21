"""
#@Time：2022/5/16-16:52
#@file：myunit
#@Project:Pythonselenium
#@Content:

"""
import logging
import unittest
from time import sleep

from Appium1.appium_advance.page_object.desired_caps import appium_desired


class Startup(unittest.TestCase):
    def setUp(self):
        logging.info('======setup=========')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('=====teardown========')
        sleep(5)
