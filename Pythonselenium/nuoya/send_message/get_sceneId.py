"""
#@Time：2022/5/13-10:32
#@file：get_sceneId
#@Project:python_basic05.py
#@Content:

"""
import json

import yaml


# from nuoya.comms.get_id import get_id


def get_sceneid():
    file = open("../yaml/get_sceneid.yaml", 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    sceneId = data['sceneId']
    groupno = data['groupno']
    # print(sceneId,groupno)
    return sceneId, groupno


params = {"messInID": "1907972254120719740",
          "fcCode": "",
          "groupNo": "1",
          "msgKeys": {
              "amount": "1",
              "productName": "1234",
              "file_info": "",
              "targetphone": "RC5vmch6P7EzPNMeeKVcvQ==",
              "accountName": "你好",
              "clientName": "123",
              "name": "1",
              "key": "1"
          },

          "sceneId": "1",
          "sendTime": "",
          "banTimeFlag": "Y",
          "messagereply": "0",
          "intervalTime": "",
          "ignoreSettingFlag": "Y",
          "businessCategory": "",
          "copySend": ""}
# params['messInID'] = get_id()
params['groupNo'] = get_sceneid()[1]
params['sceneId'] = get_sceneid()[0]
print(params)
data_paeams = json.dumps(params)
print(type(params), type(data_paeams))

if __name__ == '__main__':
    print(get_sceneid()[0], get_sceneid()[1])
