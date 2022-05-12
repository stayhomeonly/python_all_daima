'''
---------------------------
File Name:demp_yaml
Author:FENGXIN
date:2022/4/24-20:12
@Project : Pythonselenium


---------------------------

'''
import yaml

file = open(file='test1.yaml', encoding='utf-8')
res = yaml.load(file, Loader=yaml.FullLoader)  # Loader=yaml.FullLoader 这个可以不加但是会有警告
print(res, type(res))  # 返回字典形式的列表
for l in res:
    print(l)
