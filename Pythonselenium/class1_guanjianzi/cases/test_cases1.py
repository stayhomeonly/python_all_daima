"""
#@Time：2022/5/9-11:04
#@file：test_cases1
#@Project:Pythonselenium
#@Content:

"""
'''
1、用的时一组数据的场景
'''
import unittest
from time import sleep

from ddt import ddt, file_data

from class1_guanjianzi.ui_key.webui_key import WebKeys


@ddt
class TestCase(unittest.TestCase):
    @file_data('../data/baidu.yaml')
    def test_01(self, **kwargs):
        print(kwargs)
        wk = WebKeys(kwargs["type_"])
        wk.open(kwargs["url"])
        wk.input(**kwargs['input'])
        sleep(2)
        wk.click(**kwargs['button'])
        wk.wait(kwargs["time_"])
        wk.quit()


if __name__ == '__main__':
    unittest.main()
