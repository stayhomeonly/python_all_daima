"""
=========================
File Name:test_register01
Author:冯鑫
Date:2021/12/10-14:35
==========================
"""
'''
1、测试单条
2、数据回滚
3、追加其他case
'''
import unittest, requests
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.db_utils import DBUtils


@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'Business_Register')

    @data(*cases)
    def test_register(self, case):
        if case.case_id == 1:
            uname = eval(case.case_data)['username']

            self.db.cud("delete  from tb_user where name = %s;", (uname,))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_Register', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例{},执行失败！实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'Business_Register', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例{},成功！".format(case.case_id, case.case_title))



