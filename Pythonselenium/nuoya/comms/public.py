"""
#@Time：2022/5/13-10:32
#@file：get_sceneId
#@Project:python_basic05.py
#@Content:

"""

import yaml


def read_data(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    yaml_data = yaml.load(file, Loader=yaml.FullLoader)
    return yaml_data


def get_sceneid():

    file = open('../yaml/sceneid.yaml','r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    sceneId = data['sceneId']
    groupno = data['groupno']
    url = data['url']

    return sceneId, groupno, url


if __name__ == '__main__':
    print(read_data('../yaml/params.yaml'))
    print(get_sceneid())



