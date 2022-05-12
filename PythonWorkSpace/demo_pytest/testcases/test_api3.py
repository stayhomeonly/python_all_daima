'''
---------------------------
File Name:test_api3
Author:FENGXIN
date:2022/1/28-20:29

---------------------------

'''
import re
import os
import pytest
import requests
# 读取yml文件
from demo_pytest.testcases.yaml_util import YamlUtil


class TestApi3:
    # 类变量
    csrf_token = ''
    session = requests.session()

    def test_01_login(self):
        url = 'http://47.107.116.139/phpwind'
        responses = TestApi3.session.request('get', url)
        return_value = responses.text
        # 正则表达式
        value = re.search('name="csrf_token" value="(.*?)"', return_value)
        TestApi3.csrf_token = value.group(1)  # 1是下标
        print(responses.cookies)
        # <input type="hidden"  name="csrf_token" value="449ac084140e7fal"/>

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_yaml('test_login.yml'))
    def test_02_login(self, caseinfo):
        yqresult = caseinfo['validate']
        for result in yqresult:
            for key, value in dict(result).items():
                if key == 'eq':
                    for assert_key, assert_value in dict(value).items():
                        print(assert_key, assert_value)

        data = caseinfo['requests']['data']
        if data and isinstance(data, dict):
            for key, value in data.items():
                if key == 'csrf_token':
                    data[key] = TestApi3.csrf_token
        print(data)

        print(caseinfo['requests']['url'])

        print(caseinfo['requests']['headers'])
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['url']
        data = caseinfo['requests']['data']
        # data 是传表单（非嵌套的字典），json用于传json数据（嵌套的字典）
        headers = caseinfo['requests']['headers']
        response = TestApi3.session.request(method, url=url, data=data, headers=headers)
        return_value = response.json()  # 实际结果
        yqresult = caseinfo['validate']  # 预期结果
        for result in yqresult:
            for key, value in dict(result).items():
                if key == 'eq':
                    for assert_key, assert_value in dict(value).items():
                        print(assert_key, assert_value)
                        assert return_value[assert_key] == assert_value


if __name__ == '__main__':
    pytest.main(['-vs'])
