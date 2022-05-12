"""
=========================
File Name:New_token_order_items
Author:冯鑫
Date:2021/12/20-18:59
==========================
"""
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token
from comms.db_utils import DBUtils


@ddt
class TestOrderItems(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_order_items", 1, 1)

    @data(*cases)
    def testorderitems(self, case):
        one = self.db.find_one("select * from tb_order  order by rand() limit 1;")
        orderId = one[0]

        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, "token", get_token())
        if '#orderId#' in case.case_data:
            case.case_data = replace_data(case.case_data, "orderId", orderId)

        response = requests.post(url=case.url, post=eval(case.case_data))
        res = response.json()

        self.assertIn(case.execpt, str(res))
