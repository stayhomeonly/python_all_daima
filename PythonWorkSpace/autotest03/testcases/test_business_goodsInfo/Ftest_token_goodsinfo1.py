"""
=========================
File Name:test_goodsinfo1
Author:冯鑫
Date:2021/12/11-14:49
==========================
"""
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token
from comms.log_utils import logger


@ddt
class TestGoodsInfo(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, 'Business_token_goodsInfo_id', 1, 1)

    @data(*cases)
    def test_goods_info(self, case):
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            self.assertIn(case.expect, str(res))
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_token_goodsInfo_id', 1, 7, '失败')
            logger.error('测试案例{},测试用例标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e

        else:
            ReadExcel.write_data(DATA_FILE, 'Business_token_goodsInfo_id', 1, 7, '成功')
            logger.info('测试案例{},测试用例标题{},执行失败!实际结果'.format(case.case_id, case.case_title))
