"""
#@Time：2022/5/13-10:32
#@file：get_sceneId
#@Project:python_basic05.py
#@Content:

"""
from configparser import ConfigParser

import yaml

from nuoya.comms.constants import CONF_FILE


def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_data


def get_sceneid():
    with open('../yaml/params.yaml', 'r', encoding='utf-8') as f:

        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[0]["sceneId"]


# 从ini文件读取数据


def get_ini_data(section, option):
    try:
        cnp = ConfigParser()  # 填写核心代码
        cnp.read(CONF_FILE, encoding='utf-8')
        return cnp.get(section, option)
    except Exception as e:
        print('从ini文件读取测试数据失败!', e)


if __name__ == '__main__':
    print(read_data('../yaml/get_id.yaml')['url'])
    print(get_sceneid())

