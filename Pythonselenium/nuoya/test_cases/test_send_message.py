"""
#@Time：2022/5/13-21:28
#@file：test_send_message
#@Project:Pythonselenium
#@Content:

"""
import json
import unittest

import requests
from ddt import ddt, file_data

from nuoya.comms.db_utils import DBUtils
from nuoya.comms.get_id import get_id
from nuoya.comms.public import read_data


# unittest写法
@ddt
class TestSendMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    @file_data('../yaml/params.yaml')  # 参数化
    def test_send_message(self, **kwargs):
        # print(kwargs)
        kwargs['messInID'] = get_id()
        print(kwargs['messInID'])
        # 请求内容
        request_body = kwargs
        request_body1 = json.dumps(request_body)
        # print(request_body1)
        # 请求体
        herds = {"subscriberNo": "100003",
                 "password": "a55680c75243a20a901ad32f8ddbe130",
                 "messSource": "DMC",
                 "timestamp": "",
                 "Content-type": "application/json"}
        response = requests.post(url=read_data('../yaml/get_id.yaml')['url1'], headers=herds, data=request_body1)
        print(response)
        res = response.json()
        print(res)
        self.assertEqual(res['message'], 'ok')

        try:

            count = self.db.find_count("select * from nmp_business.t_message_sms_record where mess_in_id =%s;",
                                       ("kwargs['messInID']",))
            self.assertEqual(count, 1)
        except AssertionError as e:
            # 这里也可以加个error日志
            print("查询无此条信息")
            raise e

        # else:
        #     logging.info()可以加个日志info的


if __name__ == '__main__':
    TestSendMessage().test_send_message()
