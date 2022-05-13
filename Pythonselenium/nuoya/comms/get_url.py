"""
#@Time：2022/5/13-9:14
#@file：publics
#@Project:python_basic05.py
#@Content:

"""
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


if __name__ == '__main__':
    print(get_url())


