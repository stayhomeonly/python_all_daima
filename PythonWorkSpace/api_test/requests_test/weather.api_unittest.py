'''
---------------------------
File Name:weather.api_unittest
Author:FENGXIN
date:2022/2/10-17:12

---------------------------

'''

import unittest
import requests
from urllib import parse
from time import sleep


class WeatherTest(unittest.TestCase):
    def serUp(self):
        self.url = 'https://www.sojson.com/open/api/weather/json.shtml'

    def test_weather_beijing(self):
        data = {'city': '北京'}
        city = parse.urlencode(data).encode('utf-8')
        r = requests.get(url=self.url, params=city)
        result = r.json()

        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Success !')
        self.assertEqual(result['city', '北京'])


if __name__ == '__main__':
    unittest.main()
