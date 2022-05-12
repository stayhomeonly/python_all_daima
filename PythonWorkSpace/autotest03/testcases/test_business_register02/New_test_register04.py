"""
=========================
File Name:New_test_register04
Author:冯鑫
Date:2021/12/16-19:30
==========================
"""
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

    cases = ReadExcel.read_data_pl(DATA_FILE, "Business_Register", 1, 1)

    @data(*cases)
    def testregister(self, case):
        uname = eval(case.case_data)['username']
        email = eval(case.case_data)['email']
        phone1 = eval(case.case_data)['phone']
        if case.case_id == 1:
            self.db.cud("delete  from tb_user where name =%s or email =%s or phone =%s;", (uname, email, phone1))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:

            self.assertEqual(eval(case.expect), res)
            if case.case_id == 1:
                count = self.db.find_count('select * from tb_user where name = %s;', (uname,))
                self.assertEqual(count, 1)
        except Exception as e:
            ReadExcel.write_data(DATA_FILE, "Business_Register", case.case_id, 7, '失败')
            logger.error('测试案例{},测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "Business_Register", case.case_id, 7, '成功')
            logger.info('测试案例{},测试标题{},执行成功!'.format(case.case_id, case.case_title))
