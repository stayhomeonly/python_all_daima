"""
#@Time：2022/5/14-19:29
#@file：1
#@Project:python_basic05.py
#@Content:

"""
import yaml

with open('../yaml/params.yaml', 'r', encoding='utf-8') as f:
    get_scenID = yaml.load(f, Loader=yaml.FullLoader)
    print(get_scenID[0]['sceneId'])