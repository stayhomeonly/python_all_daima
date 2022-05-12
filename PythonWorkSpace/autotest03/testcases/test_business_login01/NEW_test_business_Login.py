"""
=========================
File Name:NEW_test_business_Login
Author:冯鑫
Date:2021/12/15-19:01
==========================
"""
import requests, unittest
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.db_utils import DBUtils


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'Business_Login')

    @data(*cases)
    def testlogin(self, case):
        uname = eval(case.case_data)['username']
        pwd = eval(case.case_data)['password']
        if case.case_id == 1:
            self.db.cud("delete from tb_user where name = %s or phone = %s or email=%s;", (uname, "18655664499", 'test@163.com'))
            self.db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",(uname, pwd, 'test@163.com',"18655664499"))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res))
            else:
                self.assertEqual(eval(case.expect),res)
        except Exception as e:
            ReadExcel.write_data(DATA_FILE, 'Business_Login', case.case_id, 7, '失败')
            logger.error('测试用例{},测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'Business_Login', case.case_id, 7, '成功')
            logger.info('测试用例{},测试标题{},执行成功'.format(case.case_id, case.case_title))
