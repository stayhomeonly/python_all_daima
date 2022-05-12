"""
=========================
File Name:test_business_goods_dalete01
Author:冯鑫
Date:2021/12/16-14:22
==========================
"""
'''
1、主流程

'''
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token, get_ini_data
from comms.db_utils import DBUtils
from comms.log_utils import logger


@ddt
class TestGoodsDelete(unittest.TestCase):
    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_goods_delete", 1, 1)

    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    @data(*cases)
    def testgoodsdelete(self, case):
        # sql = "select * from tb_goods where isPromote = 1 and goodsId != %s order by rand() limit 1;"
        # one = self.db.find_one(sql, (get_ini_data("goodsId1", "goodsId"),))
        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, "token", get_token())
        if "#goodsId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'goodsId', get_ini_data('goodsId2', 'goodsId'))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            self.assertEqual(eval(case.expect), res)
        except Exception as e:
            ReadExcel.write_data(DATA_FILE, "Business_goods_delete", case.case_id, 7, "失败")
            logger.error("测试案例{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "Business_goods_delete", case.case_id, 7, "成功")
            logger.error("测试案例{},测试标题{},执行成功".format(case.case_id, case.case_title))
