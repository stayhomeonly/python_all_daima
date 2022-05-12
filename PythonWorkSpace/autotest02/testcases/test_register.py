"""
=========================
File Name:test_register
Author:冯鑫
Date:2021/12/7-16:09
==========================
"""

from ddt import ddt, data
import unittest, requests
from autotest02.comms.excel_utils import ReadExcel
from autotest02.comms.log_utils import logger
from autotest02.comms.db_utils import DBUtils
from autotest02.comms.constants import DATA_FILE

cases = ReadExcel.read_data_all(DATA_FILE, 'register')




@ddt
class TestRegister(unittest.TestCase):

    @data(*cases)
    def test_register(self, case):
        if case.case_id == 1:  # 如果用有效边界值该为case.case_id in(1,3,10)
            username = eval(case.case_data)['username']
            password = eval(case.case_data)['password']
            re_password = eval(case.case_data)['re_password']
            phone = eval(case.case_data)['phone']
            sex = eval(case.case_data)['sex']
            birthday = eval(case.case_data)['birthday']
            qq = eval(case.case_data)['qq']
            email = eval(case.case_data)['email']
            db = DBUtils()
            db.cud('delete from tb_user where name=%s',
                   (username,))
            # db.cud('insert into tb_user(name,passwd,phone,email,sex,birthday,qq) values(%s,%s,%s,%s,%s,%s,%s);',
            #        (username, password, phone, email, sex, birthday, qq))
            db.close()

        response = requests.post(url=case.url, data=eval(case.case_data))
        res_body = response.json()
        try:
            self.assertEqual(eval(case.expect), res_body)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'register', case.case_id, 7, '失败') # 7 几列的意思
            logger.error("测试编号{},测试用例标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res_body))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'register', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例标题{},执行成功!".format(case.case_id, case.case_title))



