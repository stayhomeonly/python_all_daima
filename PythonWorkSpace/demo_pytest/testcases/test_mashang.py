'''
---------------------------
File Name:test-mashang
Author:FENGXIN
date:2022/1/27-21:05

---------------------------

'''
import time
import pytest


class TestMashang:
    def test_01_baili(self):
        time.sleep(3)
        print('百里')

    def test_02_fengxing(self):
        time.sleep(3)
        print('冯鑫')


if __name__ == '__main__':
    pytest.main(['-n=2'])
