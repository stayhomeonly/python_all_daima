"""
=========================
File Name:test_goodsinfo1
Author:冯鑫
Date:2021/12/11-14:49
==========================
"""

'''
1、测试主流程
2、数据回滚和数据验证
3、增加cases

'''
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token
from comms.log_utils import logger
from comms.db_utils import DBUtils


@ddt
class TestGoodsInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'Business_token_goodsInfo')

    @data(*cases)
    def test_goods_info(self, case):
        if '#token#' in case.case_data:
            if case.case_id == 3:  # 区分大小写
                case.case_data = replace_data(case.case_data, 'token', get_token().lower())
            if case.case_id == 4:  # 上一次的token值
                tk = get_token()
                get_token()
                case.case_data = replace_data(case.case_data, 'token', tk)
            else:
                case.case_data = replace_data(case.case_data, 'token', get_token())
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res))  # 判断响应体包含 查询成功
                # 判断查询商品条目数是否正确
                # 1、获取返回结果的条目数
                res_count = len(res["goods_tiems"])
                db_count = self.db.find_count('select * from tb_goods')
                self.assertEqual(res_count, db_count)  # 响应体的商品条目数和数据库的商品条目数做对比
            elif case.case_id in (13, 14, 15, 16, 17, 18, 19, 20, 23):
                self.assertIn(case.expect, str(res))
                res_count = len(res["goods_tiems"])
                self.assertEqual(1, res_count)
            elif case.case_id in (9, 10, 11, 12):
                self.assertIn(case.expect, str(res))  # 判断响应体包含 查询成功
                res_count = len(res["goods_tiems"])
                db_count = self.db.find_count("select * from tb_goods where isOnSale = %s and isPromote = %s;",
                                              (eval(case.case_data)["isOnSale"], eval(case.case_data)["isPromote"]))
                self.assertEqual(res_count, db_count)
            elif case.case_id in (5, 6):
                self.assertIn(case.expect, str(res))  # 判断响应体包含 查询成功
                res_count = len(res["goods_tiems"])
                db_count = self.db.find_count("select * from tb_goods where isOnSale = %s;",
                                              (eval(case.case_data)["isOnSale"],))
                self.assertEqual(res_count, db_count)
            elif case.case_id in (7, 8):
                self.assertIn(case.expect, str(res))  # 判断响应体包含 查询成功
                res_count = len(res["goods_tiems"])
                db_count = self.db.find_count("select * from tb_goods where isPromote = %s;",
                                              (eval(case.case_data)["isPromote"],))
                self.assertEqual(res_count, db_count)
            else:
                self.assertEqual(eval(case.expect), res)


        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_token_goodsInfo', case.case_id, 7, '失败')
            logger.error('测试案例{},测试用例标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e

        else:
            ReadExcel.write_data(DATA_FILE, 'Business_token_goodsInfo', case.case_id, 7, '成功')
            logger.info('测试案例{},测试用例标题{},执行成功'.format(case.case_id, case.case_title))




