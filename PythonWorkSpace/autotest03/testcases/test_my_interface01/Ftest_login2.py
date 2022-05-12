"""
=========================
File Name:test_login2
Author:冯鑫
Date:2021/12/9-17:40
==========================
"""
import unittest
import requests
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger

from ddt import ddt, data

'''
主流程
'''


@ddt
class TestLogin(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, 'Business_Login', 1, 1)

    @data(*cases)
    def test_login(self, case):
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res))
            else:
                self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_Login', case.case_id, 7, '失败')
            logger.error("测试案列{},测试用例标题{},执行失败,实际结果{}".format(case.case_id, case.case_tilte, res))
            logger.exception()
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'Business_Login', case.case_id, 7, '成功')
            logger.info("测试案列{},测试用例标题{},执行成功".format(case.case_id, case.case_title))
