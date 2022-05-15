"""
#@Time：2022/5/13-9:14
#@file：publics
#@Project:python_basic05.py
#@Content:

"""
import requests

# 获取url的方法

# file = open("../yaml/get_id.yaml", 'r', encoding='utf-8')
# data = yaml.load(file, Loader=yaml.FullLoader)
# url = data['url']
# print(url)
import yaml

# 第一种方法
# file = open('../yaml/get_id.yaml', 'r', encoding='utf-8')
# data = yaml.load(file, Loader=yaml.FullLoader)
# print(data)
# file.close()
# 第二中方法，建议用第二种，因为文件是自动关闭的
with open('../yaml/get_id.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)


# 获取单个id的方法
def get_id():
    try:
        url = data['url']
        response = requests.get(url)
        res = response.json()  # 转换为python字典格式
        # print(res, type(res))
        id = res['response']


        return id
    except Exception:
        print('获取ID出现了异常，请检查服务是否有问题')


if __name__ == '__main__':
    print(get_id())
