"""
#@Time：2022/5/13-21:28
#@file：test_send_message
#@Project:Pythonselenium
#@Content:

"""
import json

import allure
import pytest
import requests

from nuoya.comms.get_id import get_id
from nuoya.comms.public import read_data


# pytest参数化
@allure.feature("发送信息")
class Test_send_message:
    @pytest.mark.parametrize("params", read_data('../yaml/params.yaml'))  # 参数化
    def test_send_message(self, params):
        print("params")
        params['messInID'] = get_id()
        # 请求内容
        request_body = params
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
        assert res['message'], 'ok'


if __name__ == '__main__':
    Test_send_message().test_send_message()
