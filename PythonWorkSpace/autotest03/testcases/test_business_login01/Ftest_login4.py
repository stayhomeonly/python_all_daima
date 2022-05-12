"""
=========================
File Name:login1
Author:冯鑫
Date:2021/12/9-15:45
==========================
"""

'''
1、主流程
2、数据回滚和数据验证
3、追加主流程
自动化测试数据参数化的常见三种方式:
1.写在文件里，比如excel文件/csv文件，在操作文件
2.直接从数据库里捞数据使用
3.把测试数据写在配置文件里,常见的.json 和.ini配置文件,再从配置文件读取数据
'''
import requests, unittest
from ddt import ddt, data
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.db_utils import DBUtils
from comms.public_api import get_ini_data, replace_data


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
    def test_login(self, case):
        if '#name#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'username', get_ini_data('users', 'uname'))
            if case.case_id == 3:  # 用户名不存在的场景
                case.case_data = replace_data(case.case_data, 'username', get_ini_data('user3', 'name'))

        if '#pwd#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'password', get_ini_data('users', 'pwd'))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res))
            else:
                self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_Login', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例标题{},执行失败！实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'Business_Login', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例标题{},执行成功!".format(case.case_id, case.case_title))
