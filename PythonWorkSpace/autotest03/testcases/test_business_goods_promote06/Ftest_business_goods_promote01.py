"""
=========================
File Name:test_business_goods_promote013
Author:冯鑫
Date:2021/12/15-15:29
==========================
"""
import unittest, requests
import datetime
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import get_token, replace_data, get_ini_data
from comms.log_utils import logger
from comms.db_utils import DBUtils


@ddt
class TestGoodsPromote(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_goods_promote", 1, 1)

    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    @data(*cases)
    def testgoodspromote(self, case):
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, "token", get_token())
        if '#time#' in case.case_data:
            time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')  # 获取当前时间+1
            case.case_data = replace_data(case.case_data, 'promoteStartTime', time)
        if "#goodsId#" in case.case_data:
            sql = "select * from tb_goods where isPromote = 1 and isOnSale = 0 and goodsId != %s" \
                  " order by rand() limit 1;"
            one = self.db.find_one(sql, (get_ini_data("goodsId1", "goodsId"),))
            case.case_data = replace_data(case.case_data, 'goodsId', one[0])
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            self.assertEqual(eval(case.expect), res)

        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, "Business_goods_promote", case.case_id, 7, '失败')
            logger.error('测试案列{}，测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "Business_goods_promote", case.case_id, 7, '成功')
