"""
=========================
File Name:test_business_items1
Author:冯鑫
Date:2021/12/13-16:49
==========================

"""
'''
1、主流程
2、增加其他case和数据回滚和数据验证
'''
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token
from comms.log_utils import logger
from comms.db_utils import DBUtils


@ddt
class TestGoodsItems(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'Business_order_items')

    @data(*cases)
    def test_order_items(self, case):
        one = self.db.find_one("select * from tb_order  order by rand() limit 1;")
        orderId = one[0]
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if '#orderId#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'orderId', orderId)
        if case.case_id == 4:
            self.db.cud('delete from tb_order where orderId = %s',(eval(case.case_data)['orderId']))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            if case.case_id == 1:
                # 四表链接查询orderId数据,如果查询多条和goods_tiems比较,如果查询到数据,断言响应体包含查询成功,反之断言响应体包含查询无结果
                sql = "select * from tb_user u,tb_order o,tb_goods g,tb_order_goods og where u.userId = o.userId " \
                      "and o.orderId = og.orderId and og.goodsId = g.goodsId and o.orderId = %s;"
                count = self.db.find_count(sql, (orderId,))
                if count > 0:
                    self.assertEqual(count, len(res['goods_tiems']))
                    self.assertIn('查询成功', str(res))
                elif count == 0:
                    self.assertIn('查询无结果', str(res))
                else:
                    self.assertEqual(eval(case.expect), res)


            else:
                self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_order_items', case.case_id, 7, '失败')
            logger.error('测试案例{},测试用例标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e

        else:
            ReadExcel.write_data(DATA_FILE, 'Business_order_items',case.case_id, 7, '成功')
            logger.info('测试案例{},测试用例标题{},执行成功!'.format(case.case_id, case.case_title))
