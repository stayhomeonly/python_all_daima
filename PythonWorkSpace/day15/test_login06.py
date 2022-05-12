"""
=========================
File Name:test_login06
Author:冯鑫
Date:2021/12/6-15:51
==========================
"""
from ddt import ddt, data
import unittest, requests
from day15.excel_utils05 import ReadExcel

cases = ReadExcel.read_data_all(r'cases.xlsx', 'Login')


@ddt
class TestLogin(unittest.TestCase):  # 测试需要继承unittest.TestCase类，这是当前类就是测试类
    @data(*cases)
    def test_login(self, case):
        response = requests.post(url=case.url,
                                 data=eval(case.case_data))  # 识别()中的python表达式，把字符串转成了字典
        res_body = response.json()  # res_body就是接口响应的实际结果
        self.assertEqual(eval(case.expect), res_body)
