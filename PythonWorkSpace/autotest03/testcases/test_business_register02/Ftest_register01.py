"""
=========================
File Name:test_register01
Author:冯鑫
Date:2021/12/10-14:35
==========================
"""
import unittest, requests
from ddt import ddt, data
from autotest03.comms.excel_utils import ReadExcel
from autotest03.comms.constants import DATA_FILE
from autotest03.comms.log_utils import logger


@ddt
class TestRegister(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, 'Business_Register', 1, 1)

    @data(*cases)
    def test_register(self, case):
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_Register', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例{},执行失败！实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'Business_Register', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例{},成功！".format(case.case_id, case.case_title))






