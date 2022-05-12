"""
#@Time：2022/5/9-13:07
#@file：yaml_dump
#@Project:Pythonselenium
#@Content:

"""

# json.load(文件)是把json转换成字典形式，json.dump()是把字典转换为json，
# yaml.load()是把yaml转换为python类型的数据，yaml.dump()是把其中数据类型，转换为yaml格式
import yaml

slogan = ["welcome", 'to', '51zxw']
website = {'url': 'www.51zxw.net'}

print(slogan)
print(website)

print(yaml.dump(slogan))
print(yaml.dump(website))
