"""
#@Time：2022/5/8-17:20
#@file：yaml.load
#@Project:Pythonselenium
#@Content:

"""
import yaml

file = open("familyInfo.yaml", 'r', encoding='utf-8')
data = yaml.load(file,Loader=yaml.FullLoader)
print(data)
print(data['name'])
print(data['age'])

print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'][0]['name'])
print(data['children'][0]['age'])

print(data['children'][1]['name'])
print(data['children'][1]['age'])