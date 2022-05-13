"""
#@Time：2022/5/13-9:38
#@file：get_id
#@Project:python_basic05.py
#@Content:

"""
import requests

from get_url import get_url

# 获取单个id的方法
def get_id():
    url = get_url()
    response = requests.get(url)
    res = response.json()  # 转换为python字典格式
    # print(res, type(res))
    id = res['response']

    return id


if __name__ == '__main__':
    print(get_id())
