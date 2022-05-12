"""
=========================
File Name:test_info
Author:冯鑫
Date:2021/12/9-14:02
==========================
"""
from ddt import ddt, data
import unittest, requests
from autotest02.comms.excel_utils import ReadExcel
from autotest02.comms.log_utils import logger
from autotest02.comms.db_utils import DBUtils
from autotest02.comms.constants import DATA_FILE

cases_login = ReadExcel.read_data_pl(r'D:\PythonWorkSpace\autotest02\data\cases1.xlsx', 'Login', 1, 1)
cases_info = ReadExcel.read_data_all(r'D:\PythonWorkSpace\autotest02\data\cases1.xlsx', 'Info')


@ddt
class TestInfo(unittest.TestCase):  # 测试需要继承unittest.TestCase类，这是当前类就是测试类
    @data(*cases_info)
    def test_info(self, case):

        response = requests.post(url=cases_login[0].url,
                                 data=eval(cases_login[0].case_data))  # 思路先是获取登陆的token值,再把获取的token值赋值
        # 给goods_info里面的token使用,如果得出来的结果还是一样,则说明成功
        res_body = response.json()  # res_body就是接口响应的实际结果
        tk = res_body['token']

        case_data = eval(case.case_data)
        case_data["token"] = tk
        response1 = requests.post(url=case.url, data=case_data)
        res_body1 = response1.json()

        try:
            self.assertEqual(eval(case.excepted), res_body1)  # assert 断言的意思，Equal是相等的意思
        except AssertionError as e:
            ReadExcel.write_data(r'D:\PythonWorkSpace\autotest02\data\cases1.xlsx', 'Info', 'Login', case.case_id, 7,
                                 '失败')
            logger.error('测试编号{},测试用例标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res_body))
            logger.exception(e)
            raise e  # 提交错误

        else:
            ReadExcel.write_data(r'D:\PythonWorkSpace\autotest02\data\cases1.xlsx', 'Info', case.case_id, 7, '成功')
            logger.info('测试编号{},测试用例标题{},执行成功!'.format(case.case_id, case.case_title))
