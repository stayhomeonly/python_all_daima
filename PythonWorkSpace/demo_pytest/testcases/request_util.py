'''
---------------------------
File Name:request_util.py
Author:FENGXIN
date:2022/1/25-13:54

---------------------------

'''

import requests


class RequestUtil:
    # 统一的入口和接口
    def send_requests(self, method, url, data, **kwargs):
        # print("这是所有接口请求的入口和出口")
        print('method:' + str(method))  # None 不能当字符串
        print('url:' + str(url))
        print('data:' + str(data))
        method = str(method).lower()  # 把method全部转换为小写，因为有的时候method不一定是小写
        res = None
        if method == 'get':
            res = requests.get(url=url, params=data)
        elif method == 'post':
            res = requests.post(url=url, json=data)
        else:
            print('不支持的请求')
        return res
