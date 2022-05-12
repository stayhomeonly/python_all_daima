"""
=========================
File Name:python_basic21
Author:pengyumei
Date:2021/12/3-10:04
==========================
"""
import requests

# 发送get请求
response = requests.get(url='https://www.baidu.com/')
# res_body =response.text  # 获取响应方式1,这个是文本格式,但是扩展为html为乱码,不建议用
res_body = response.content.decode('utf-8')
print(res_body)

# 案例: 通过requests 调用我们自己的接口
res = requests.get(url='http://127.0.0.1:5000/register?username=xiaowang&password=a123456&'
                       're_password=a123456&email=11267@qq.com&phone=15161039043')
res_body = res.content.decode('utf-8')
print(res_body)  # {"code": 9999, "msg": "注册成功"}

# 发送post请求
# 注意:发送post请求,因为请求数据放在请求体中,所以需要传入一个字典,存放请求数据
post = requests.post(url='http://127.0.0.1:5000/user_login',
                     data={'username': 'xiaowang', 'password': 'a123456'})
res_body = post.content.decode('utf-8')
print(res_body)
