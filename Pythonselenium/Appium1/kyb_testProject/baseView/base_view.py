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

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动的方法
    def swipe(self, start_x, start_y, end_x, end_y, duration):#duration滑动持续的时间
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
