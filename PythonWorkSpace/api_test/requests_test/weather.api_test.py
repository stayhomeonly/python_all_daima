'''
---------------------------
File Name:weather.api_test
Author:FENGXIN
date:2022/2/9-15:30

---------------------------

'''
import requests
from urllib import parse

data = {'city': '北京'}
city = parse.urlencode(data).encode('utf-8')  # 参数编码
url = 'https://www.sojson.com/open/api/weather/json.shtml'

r = requests.get(url, params=city)
# print(r.text)

response_data = r.json()
print(response_data.data['date'])
print(response_data.data['message'])
print(response_data.data['status'])
print(response_data.data['city'])

print(response_data['data']['forecast'][0]['date'])
print(response_data['data']['forecast'][0]['type'])
print(response_data['data']['forecast'][0]['high'])
print(response_data['data']['forecast'][0]['low'])
