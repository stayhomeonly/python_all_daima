"""
=========================
File Name:test_business_token_goods_input01
Author:冯鑫
Date:2021/12/14-15:23
==========================
"""
'''
1、主流程
2、数据回滚和数据验证
'''
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import get_token, replace_data
from comms.log_utils import logger
from comms.db_utils import DBUtils


@ddt
class TestGoodsInput(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_goods_input",1,1)

    @data(*cases)
    def test_goods_input(self, case):
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, "token", get_token())
        # 正确流程
        if case.case_id == 1:
            self.db.cud("delete from tb_goods where goodsName = %s;", (eval(case.case_data)['goodsName'],))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            self.assertEqual(eval(case.expect), res)
            if case.case_id == 1:

                #数据验证
                count = self.db.find_count("select *  from tb_goods where goodsName = %s;",
                                               (eval(case.case_data)['goodsName'],))
                self.assertEqual(1, count)

        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, "Business_goods_input", case.case_id, 7, '失败')
            logger.error('测试案例{},测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e

        else:
            ReadExcel.write_data(DATA_FILE, "Business_goods_input", case.case_id, 7, '成功')
            logger.info('测试案例{},测试标题{},执行成功!'.format(case.case_id, case.case_title))
