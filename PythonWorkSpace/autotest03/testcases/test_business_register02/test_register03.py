"""
=========================
File Name:test_register01
Author:冯鑫
Date:2021/12/10-14:35
==========================
"""
'''
1、测试单条
2、数据回滚和数据验证,验证必须在数据执行后进行
3、追加case
'''
import unittest, requests
from ddt import ddt, data
from autotest03.comms.excel_utils import ReadExcel
from autotest03.comms.constants import DATA_FILE
from autotest03.comms.log_utils import logger
from autotest03.comms.db_utils import DBUtils


@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'Business_Register')

    @data(*cases)  # 参数化 读取到的内容赋值给case
    def test_register(self, case):
        uname = eval(case.case_data)["username"]
        email = eval(case.case_data)["email"]
        phone = eval(case.case_data)["phone"]
        pwd = eval(case.case_data)["password"]
        # 正确流程
        if case.case_id in (1, 3, 9):
            self.db.cud("delete from tb_user where name = %s or email = %s or phone = %s;", (uname, email, phone))
        if case.case_id == 7:  # 用户名已注册的场景
            self.db.cud("delete from tb_user where name = %s or email = %s or phone = %s;", (uname, email, phone))
            self.db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                        (uname, pwd, 'test23code@163.com', '14755556666'))
        if case.case_id == 32:  # 邮箱已注册的场景,用户名和手机号不重复
            self.db.cud("delete from tb_user where name = %s or email = %s or phone = %s;", (uname, email, phone))
            self.db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                        ("testhua9", pwd, email, '14755556669'))
        if case.case_id == 33:  # 手机号已注册的场景,用户名和邮箱不重复
            self.db.cud("delete from tb_user where name = %s or email = %s or phone = %s;", (uname, email, phone))
            self.db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                        ("testhua8", pwd, 'test23code33@163.com', phone))

            self.db.cud("delete  from tb_user where name = %s or email=%s or phone = %s;", (uname, email, phone))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)
            # 数据验证
            if case.case_id in (1, 3, 9):
                count = self.db.find_count("select * from tb_user where name=%s;", (uname,))
                self.assertEqual(1, count)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'Business_Register', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例{},执行失败！实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'Business_Register', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例{},成功！".format(case.case_id, case.case_title))
