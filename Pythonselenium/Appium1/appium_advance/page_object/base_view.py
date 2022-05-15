"""
#@Time：2022/5/15-13:47
#@file：base_view
#@Project:python_basic05.py
#@Content:

"""


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
