"""
=========================
File Name:python_basic22
Author:pengyumei
Date:2021/12/3-11:38
==========================
"""
import requests
import json

'''
requests 模拟json格式的请求(请求数据为json格式的请求)

'''
# 发送json请求的三个入参
# 1.url
# 2.json格式的请求参数(使用json.dumps(入参),把字典类型转换为json格式)
# 3.必须要添加请求头信息:"Content-Type":"application/json" 表明请求体数据的内容为json格式

response = requests.post(url='http://127.0.0.1:6666/business/regist_json',
                         data=json.dumps({"username": "xiaoxu",
                                          "password": "a123456",
                                          "re_password": "a123456",
                                          "phone": "17744556699",
                                          "sex": "",
                                          "birthday": "",
                                          "qq": "",
                                          "email": "888@qq.com"
                                          }, ensure_ascii=False),
                         headers={"content-Type": "application/json"})

res_body = response.json()
print(res_body)
