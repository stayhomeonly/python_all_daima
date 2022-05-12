'''
---------------------------
File Name:test_api1
Author:FENGXIN
date:2022/1/23-15:43

---------------------------

'''

import pytest
import time
import os

from demo_pytest.testcases.request_util import RequestUtil

db = RequestUtil()

from demo_pytest.testcases.yaml_util import YamlUtil


class TestApi:
    assert_token = None

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_yaml('get_token.yml'))
    def test_01_get_token1(self, caseinfo):
        # print(caseinfo['name'])
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['url']
        data = caseinfo['requests']['data']
        # print(caseinfo['validate'])

        res = db.send_requests(method=method, url=url, data=data)

        return_data = res.json()
        print(return_data)
        try:
            TestApi.assert_token = return_data["assert_token"]
        except Exception as e:
            pass
        # 数据驱动，在yml文件中添加即可

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_yaml('edit_flag.yml'))
    def test_02_edit_flag(self, caseinfo):
        url = caseinfo['requests']['url'] + "?assert_token" + TestApi.assert_token
        data = caseinfo['requests']['data']
        method = caseinfo['requests']['method']

        res = RequestUtil().send_requests(method=method, url=url, data=data)
        print(res.json())

    # @pytest.mark.parametrize('name,age', [['百里', 13], ['星耀', 10], ['依然', 12]])
    # def test_01_get_token2(self, name, age):
    #     print('获取鉴权码接口:' + name, age)


