'''
---------------------------
File Name:requests_basic
Author:FENGXIN
date:2022/2/3-17:49

---------------------------

'''
import json

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

base_url = "http://httpbin.org"
# r = requests.get(base_url + '/get')
# print(r.status_code) # 响应状态码
#
# r = requests.post(base_url + '/post')
# print(r.status_code)
#
# r = requests.put(base_url + '/put')
# print(r.status_code)
#
# r = requests.delete(base_url + '/delete')
# print(r.status_code)


# 参数传递
# param_data = {'user': 'zxw', 'password': '6666'}
# r = requests.get(base_url + '/get', params=param_data)
# print(r.url)
#
# print(r.status_code)

# form_data = {'user': '51zxw', 'password': '8888'}
# r = requests.post(base_url+'/post', data=form_data)
# print(r.text)

# 请求头定制
# form_data = {'user': '51zxw', 'password': '8888'}
# header = {'user-agent': 'Mozilla/5.0'}
# r = requests.post(url=base_url + '/post', data=form_data, headers=header)
# print(r.text)

# cookie设置
# cookie = {'user': '51zxw'}
# r = requests.get(base_url + '/cookies', cookies=cookie, timeout=3) # 设置超时
# print(r.text)

# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# print(type(r.cookies))
# for key, value in r.cookies.items():
#     print(key + ':' + value)

# 文件上传
# file = {'file': open('zxw_logo.png', 'rb')}  # 文件名称在一个目录下，如果不在请写相对路径或者绝对路径
# r = requests.post(base_url + '/post', files=file)
# print(r.text)

# r = requests.get(base_url+'/cookies/set/user/51zxw')
# print(r.text)
#
# r = requests.get(base_url+'/cookies')
# print(r.text)

# 会话对象
# s = requests.Session()
# r = s.get(base_url+'/cookies/set/user/51zxw')
# print(r.text)
#
# r =s.get(base_url+'/cookies')
# print(r.text)


# 证书验证


# r = requests.get('https://www.12306.cn', verify=False)
# print(r.text)


# 代理设置
# proxies = {'http': 'http://219.141.153.41:80'}
# r = requests.get(base_url + '/get', proxies=proxies)
# print(r.text)

# 身份验证
# r = requests.get(base_url+'/basic-auth/51zxw/8888',auth=HTTPBasicAuth('51zxw','8888'))
# print(r.text)

# r = requests.get(base_url+'/digest-auth/auth/zxw/6666',auth=HTTPDigestAuth('zxw','6666'))
# print(r.text)

# 流式请求
r = requests.get(base_url + '/stream/10', stream=True)
# num 表示返回结果集的数量，比如输入 10 则会返回 10 个下面这种不同 id 的结果
# 针对这种类型的接口我们对结果集的处理需要使用迭代方法 iter_lines()来处理,具体使用如下：

if r.encoding is None:
    r.encoding = 'utf-8'
for line in r.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(data["id"])