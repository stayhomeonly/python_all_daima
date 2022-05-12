"""
=========================
File Name:public_api
Author:冯鑫
Date:2021/12/10-16:56
==========================
"""

from configparser import ConfigParser

import requests

from comms.constants import CONF_FILE


# 从ini文件获取数据
def get_ini_data(section, option):  # section 部分，option ，选项
    try:
        cnp = ConfigParser()
        cnp.read(CONF_FILE, encoding="utf-8")
        return cnp.get(section, option)
    except Exception as e:
        print('从ini文件读取测试数据失败！', e)


# 数据替换
def replace_data(my_dict, key, value):

    """
    :param my_dict: 需要替换的字符串类型的字典
    :param key: 需要替换的键
    :param value: 替换的数据
    :return: 替换后的字符串类型的字典
    """
    dict1 = eval(my_dict)
    dict1[key] = value
    return str(dict1)


# 获取token值
def get_token():
    try:
        response = requests.post(url='http://127.0.0.1:6666/business/token_login',
                                 data={'username': get_ini_data('user2', 'name'),
                                       'password': get_ini_data('user2', 'password'),
                                       'typeId': '101'})

        res = response.json()
        return res['token']
    except Exception as e:
        print('获取token失败!', e)


if __name__ == '__main__':
    print(get_token())