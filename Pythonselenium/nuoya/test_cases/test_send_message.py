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

from nuoya.comms.get_id import get_id
from nuoya.comms.public import read_data

# unittest写法
@ddt
class Test_send_message(unittest.TestCase):
    @file_data('../yaml/params.yaml')  # 参数化
    def test_send_message(self, **kwargs):
        print(kwargs)
        kwargs['messInID'] = get_id()
        # 请求内容
        request_body = kwargs
        request_body1 = json.dumps(request_body)
        print(request_body1)
        # 请求体
        herds = {"subscriberNo": "100003",
                 "password": "a55680c75243a20a901ad32f8ddbe130",
                 "messSource": "DMC",
                 "timestamp": "",
                 "Content-type": "application/json"}
        response = requests.post(url=read_data('../yaml/sceneid.yaml')['url'], headers=herds, data=request_body1)
        print(response)
        res = response.json()
        print(res)
        self.assertEqual(res['message'], 'ok')


if __name__ == '__main__':
    Test_send_message().test_send_message()
