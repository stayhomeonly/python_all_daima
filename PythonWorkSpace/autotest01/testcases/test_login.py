"""
=========================
File Name:test_login07
Author:冯鑫
Date:2021/12/6-16:02
==========================
"""
from ddt import ddt, data
import unittest, requests
from autotest01.comms.excel_utils import ReadExcel
from autotest01.comms.log_utils import logger
from autotest01.comms.db_utils import DBUtils

cases = ReadExcel.read_data_all(r'D:\PythonWorkSpace\autotest01\data\cases.xlsx', 'Login')

@ddt
class TestLogin(unittest.TestCase):  # 测试需要继承unittest.TestCase类，这是当前类就是测试类
    @data(*cases)
    def test_login(self, case):
        # 正确流程回滚
        if case.case_id == 1:
            uname = eval(case.case_data)['username']
            pwd = eval(case.case_data)['password']
            db = DBUtils()
            db.cud('delete from tb_user where name = %s;', (uname,))
            db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);',
                   (uname, pwd, "test23@163.com", '15995654411'))
            db.close()
        response = requests.post(url=case.url,
                                 data=eval(case.case_data))  # 识别()中的python表达式，把字符串转成了字典
        res_body = response.json()  # res_body就是接口响应的实际结果
        try:
            self.assertEqual(eval(case.expect), res_body)  # assert 断言的意思，Equal是相等的意思
        except AssertionError as e:
            ReadExcel.write_data(r'D:\PythonWorkSpace\autotest01\data\cases.xlsx', 'Login', case.case_id, 7, '失败')
            logger.error('测试编号{},测试用例标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title,res_body))
            logger.exception(e)
            raise e  # 提交错误

        else:
            ReadExcel.write_data(r'D:\PythonWorkSpace\autotest01\data\cases.xlsx', 'Login', case.case_id, 7, '成功')
            logger.info('测试编号{},测试用例标题{},执行成功!'.format(case.case_id, case.case_title))
