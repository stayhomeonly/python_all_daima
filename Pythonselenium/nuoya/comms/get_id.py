"""
#@Time：2022/5/13-9:14
#@file：publics
#@Project:python_basic05.py
#@Content:

"""
import requests
import yaml


# 获取url的方法

# file = open("../yaml/get_id.yaml", 'r', encoding='utf-8')
# data = yaml.load(file, Loader=yaml.FullLoader)
# url = data['url']
# print(url)

def get_url():
    file = open("../yaml/get_id.yaml", 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    url = data['url']
    # print(url)
    return url


# 获取单个id的方法
def get_id():
    url = get_url()
    response = requests.get(url)
    res = response.json()  # 转换为python字典格式
    # print(res, type(res))
    id = res['response']

    return id


if __name__ == '__main__':
    print(get_url(), get_id())
