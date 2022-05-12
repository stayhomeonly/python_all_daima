"""
=========================
File Name:python_senior23
Author:冯鑫
Date:2021/12/3-11:56
==========================
"""
import requests

'''
requests模拟接口之间的关联,一个接口的入参是另一个接口的入参
'''

# 1、先进行登录
response = requests.post(url="http://127.0.0.1:6666/business/token_login",
                         data={"username": "xiaoxu", "password": "a123456", "typeId": "101"})

res_body = response.json()  # 获取json格式的响应体数据
print(res_body)
tk = res_body['token']  # 获取json数据格式中的token键对应的值，并且保存tk变量组
#tk = res_body.get("token")另外一种写法
print(tk)

# 2、在调用商品信息查询接口
# post=requests.post(url='http://127.0.0.1:6666/business/token_goodsInfo',
#                    data={'token':tk,"goodsID":"","isOnSale":"","inPromate":""})
response=requests.get(url="http://127.0.0.1:6666/business/token_goodsInfo?token=%s"
                          "&goodsID=''&isOnSal=''&inPromate=''"% tk)
res=response.json()
print(res)
