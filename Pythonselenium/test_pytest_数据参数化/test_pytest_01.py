"""
--------------------------------
@Time  : 2022/2/24-------14:43
@author  :  ztt
@File  :  python_basic02 
--------------------------------
"""
"""
注册，使用参数数据化，使测试数据和逻辑分离
"""
import pytest
import requests


class TestRegister:
    cases = [{"case_data": "{'username':'xiaoli','password':'a123456',""'phone':'15899885566','re_password':'a123456',"
                           "'email':'1218@qq.com'}", "exp": "{'code':9999,'msg':'注册成功'}"},
             {"case_data": "{'username':'','password':'a123456',""'phone':'15899885578','re_password':'a123456',"
                           "'email':'15878@qq.com'}", "exp": "{'code':1001,'msg':'用户名不能为空'}"},
             {"case_data": "{'username':'xiaoji','password':'',""'phone':'15899885447','re_password':'a123456',"
                           "'email':'12008@qq.com'}", "exp": "{'code': 1002,'msg':'密码不能为空'}"},
             {"case_data": "{'username':'xiaoniu','password':'a123456','phone':'15899885523','re_password':'a123456',"
                           "'email':''}", "exp": "{'code':1005,'msg':'邮箱不能为空'}"},
             {"case_data": "{'username':'xiaohh','password':'a123456','phone':'','re_password':'a123456',"
                           "'email':'15688@qq.com'}", "exp": "{'code':1006,'msg':'手机号不能为空'}"},

             {"case_data": "{'username':'xiaoll','password':'a123456','phone':'15899844566','re_password':'a123456',"
                           "'email':'187418qq.com'}", "exp": "c"}, ]

    @pytest.mark.parametrize("case", cases)
    def test_register(self, case):
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data=eval(case["case_data"]))
        res = response.json()
        assert eval(case["exp"]) == res


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest_01.py'])
