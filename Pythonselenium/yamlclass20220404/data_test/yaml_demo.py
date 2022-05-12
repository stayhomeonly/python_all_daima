'''
---------------------------
File Name:yaml_demo
Author:FENGXIN
date:2022/4/4-16:40

---------------------------

'''
import yaml

# 读取文件
file = open('../data/data2.yaml', 'r', encoding='utf-8')

data = yaml.load(stream=file, Loader=yaml.FullLoader)
# 数据类型的展示
print(type(data))

# 数据内容的展示
print(data)


