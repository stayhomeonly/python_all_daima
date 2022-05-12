"""
--------------------------------
@Time  : 2022/2/24-------15:51
@author  :  ztt
@File  :  python_basic02 
--------------------------------
"""
import pytest
import requests


# 创建一个类，将测试用例写道cases中
class TestLogin:
    cases = [{"case_data": "{'username':'laoliu','password':'ab12345'}",
              "exp": "{'code': 9999, 'msg': '登录成功'}"},
             {"case_data": "{'username':'','password':'ab12345'}",
              "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
             {"case_data": "{'username':'laoliu','password':''}",
              "exp": "{'code': 1002, 'msg': '密码不能为空'}"}]

    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/user_login',
                                 data=eval(case["case_data"]))
        res = response.json()
        assert eval(case["exp"]) == res


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest_02.py'])
