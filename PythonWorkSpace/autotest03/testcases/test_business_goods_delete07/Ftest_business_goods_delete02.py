"""
=========================
File Name:test_business_goods_dalete01
Author:冯鑫
Date:2021/12/16-14:22
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


        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, "token", get_token())
        if "#goodsId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'goodsId', get_ini_data('goodsId2', 'goodsId'))
        if case.case_id == 1:
            self.db.cud("INSERT INTO `businessdb`.`tb_goods` "
                        "(`goodsId`, `goodsName`, `goodsTypeId`, `descp`, `num`, "
                        "`onTime`, `offTime`, `shopPrice`, `promotePrice`, `promoteStartTime`, "
                        "`promoteEndTime`, `isOnSale`, "
                        "`isPromote`, `givePoints`) VALUES"
                        " (%s, '天下非公开', '44444', '非常好吃，想再来一包', '88888888', "
                        "'2021-12-14 19:07:36', '2099-12-31', '0.00', '0.00', NULL, NULL, '1', NULL, '10');"
                        , (get_ini_data('goodsId2', 'goodsId'),))
        # if case.case_id == 1:
        #     self.db.cud("INSERT INTO `businessdb`.`tb_goods` (`goodsId`, `goodsName`, `goodsTypeId`, `descp`,"
        #                     " `num`, `onTime`, `offTime`, `shopPrice`, `promotePrice`, `promoteStartTime`, "
        #                     "`promoteEndTime`, `isOnSale`, `isPromote`, `givePoints`) VALUES (%s, '卫龙辣条07',"
        #                     " '10004', '好面好劲道,Q弹爽口,回味无穷。美味从此刻定义', '50000', '2021-12-15 11:49:14',"
        #                     " '2099-12-31', '2.50', '0.00', NULL, NULL, '1', '1', '10');",
        #                     (get_ini_data('goodsId2', 'goodsId'),))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:

            self.assertEqual(eval(case.expect), res)
            # 数据验证
            if case.case_id == 1:
                count = self.db.find_count("select * from tb_goods where goodsId = %s;",
                                           (get_ini_data('goodsId2', 'goodsId'),))
                self.assertEqual(0, count)




        except Exception as e:
            ReadExcel.write_data(DATA_FILE, "Business_goods_delete", case.case_id, 7, "失败")
            logger.error("测试案例{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "Business_goods_delete", case.case_id, 7, "成功")
            logger.error("测试案例{},测试标题{},执行成功".format(case.case_id, case.case_title))


# @ddt
# class TestGoodsDelete(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.db = DBUtils()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.db.close()
#
#     cases = ReadExcel.read_data_pl(DATA_FILE, 'Business_goods_delete', 1, 1)
#
#     @data(*cases)
#     def test_goods_delete(self, case):
#         if "#token#" in case.case_data:
#             case.case_data = replace_data(case.case_data, 'token', get_token())
#         if "#goodsId#" in case.case_data:
#             case.case_data = replace_data(case.case_data, 'goodsId', get_ini_data('goodsId2', 'goodsId'))
#
#         if case.case_id == 1:
#             self.db.cud("INSERT INTO `businessdb`.`tb_goods` (`goodsId`, `goodsName`, `goodsTypeId`, `descp`,"
#                         " `num`, `onTime`, `offTime`, `shopPrice`, `promotePrice`, `promoteStartTime`, "
#                         "`promoteEndTime`, `isOnSale`, `isPromote`, `givePoints`) VALUES (%s, '卫龙辣条07',"
#                         " '10004', '好面好劲道,Q弹爽口,回味无穷。美味从此刻定义', '50000', '2021-12-15 11:49:14',"
#                         " '2099-12-31', '2.50', '0.00', NULL, NULL, '1', '1', '10');",
#                         (get_ini_data('goodsId2', 'goodsId'),))
#
#         response = requests.post(url=case.url, data=eval(case.case_data))
#         res = response.json()
#
#         try:
#             self.assertEqual(eval(case.expect), res)
#             if case.case_id == 1:
#                 count = self.db.find_count("select * from tb_goods where goodsId = %s;",
#                                            (get_ini_data('goodsId2', 'goodsId'),))
#                 self.assertEqual(0, count)
#         except AssertionError as e:
#             ReadExcel.write_data(DATA_FILE, 'Business_goods_delete', case.case_id, 7, '失败')
#             logger.error("测试编号{},测试用例标题{},执行失败！实际结果{}".format(case.case_id, case.case_title, res))
#             logger.exception(e)
#             raise e
#         else:
#             ReadExcel.write_data(DATA_FILE, 'Business_goods_delete', case.case_id, 7, '成功')
#             logger.info("测试编号{},测试用例标题{},执行成功!".format(case.case_id, case.case_title))
