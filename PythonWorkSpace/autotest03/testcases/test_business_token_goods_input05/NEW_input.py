"""
=========================
File Name:NEW_input
Author:冯鑫
Date:2021/12/21-19:56
==========================
"""
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.public_api import get_token, replace_data


@ddt
class TestGoodsInput(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_goods_input", 1, 1)

    @data(*cases)
    def testgoodsinput(self, case):
        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, "Business_goods_input", case.case_id, 7, "失败")
            logger.error("测试案例{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "Business_goods_input", case.case_id, 7, "成功")
            logger.info("测试案例{},测试标题{},执行成功!".format(case.case_id, case.case_title))
