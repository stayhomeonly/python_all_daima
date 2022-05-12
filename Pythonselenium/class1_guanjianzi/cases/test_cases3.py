"""
#@Time：2022/5/9-20:16
#@file：test_case3
#@Project:Pythonselenium
#@Content:

"""
'''
1、用的时一组数据的场景
2、追加多组数据的场景，且每组数据自动运行，关闭
'''
import unittest
from time import sleep

from ddt import ddt, file_data

from class1_guanjianzi.ui_key.webui_key import WebKeys


@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        self.wk = WebKeys('Chrome')
        self.wk.open('http://www.baidu.com')

    def tearDown(self):
        self.wk.quit()

    @file_data('../data/baidu1.yaml') # 基于@file_data读出来的数据就是字典格式，就用字典的变量来接收
    def test_01(self, **kwargs):
        print(kwargs)

        self.wk.input(**kwargs['input']) # 传入一个字典才用**kwargs参数
        sleep(2)
        self.wk.click(**kwargs['button'])
        self.wk.wait(kwargs["time_"]) # 传入一个值参数话


if __name__ == '__main__':
    unittest.main()
