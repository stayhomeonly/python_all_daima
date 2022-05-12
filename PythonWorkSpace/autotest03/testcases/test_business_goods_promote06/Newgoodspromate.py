"""
=========================
File Name:Newgoodspromate
Author:冯鑫
Date:2021/12/23-18:56
==========================
"""
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token, get_ini_data
from comms.db_utils import DBUtils
from comms.log_utils import logger


@ddt
class TestGoodsPromate(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, 'Business_goods_promote', 1, 1)

    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    @data(*cases)
    def testgoodspromate(self, case):

        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, "token", get_token())
        if '#goodsId' in case.case_data:
            sql = "select * from tb_goods where inOnsale =1 and ispromote= 0 and goodsId != %s" \
                  "order by rand limit 1"
            one = self.db.find_one(sql, get_ini_data('goodsId1', 'goodsId'))
            case.case_data = replace_data(case.case_data, "goodsId", one[0])

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:

            self.assertEqual(eval(case.expect), res)

        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_goods_promote', case.case_id, 7, '失败')
            logger.error("测试案例{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_tiitle, res))
            logger.exception(e)
            raise e

        else:
            ReadExcel.write_data(DATA_FILE, 'Business_goods_promote', case.case_id, 7, "成功")
            logger.info("测试案例{},测试标题{},执行成功".format(case.case_id, case.case_tiitle))
