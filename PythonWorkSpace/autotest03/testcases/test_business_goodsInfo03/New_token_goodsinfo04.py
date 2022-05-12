"""
=========================
File Name:New_token_goodsinfo04
Author:冯鑫
Date:2021/12/18-13:50
==========================
"""
from ddt import ddt, data
import requests, unittest
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token
from comms.log_utils import logger


@ddt
class TokenGoodsInfo(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_token_goodsInfo", 1, 1)

    @data(*cases)
    def test_goods_info(self, case):
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertIn(case.expect, str(res))

        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_token_goodsInfo', case.case_id, 7, '失败')
            logger.error('测试案例{},测试用例标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e

        else:
            ReadExcel.write_data(DATA_FILE, 'Business_token_goodsInfo', case.case_id, 7, '成功')
            logger.info('测试案例{},测试用例标题{},执行成功!'.format(case.case_id, case.case_title))
