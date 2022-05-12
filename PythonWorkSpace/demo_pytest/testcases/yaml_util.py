'''
---------------------------
File Name:yaml_util.py
Author:FENGXIN
date:2022/1/23-16:35

---------------------------

'''
import os
import yaml


class YamlUtil:
    # 读取yaml文件的方法
    def read_yaml(self, yml_name):
        with open(os.path.dirname(os.path.dirname(__file__)) + '/testcases/' + yml_name, encoding='utf-8') as f:
            # os.path.dirname(os.path.dirname(__file__)) 和 os.getcwd()用法一致
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value


print(YamlUtil().read_yaml('get_token.yml'))
