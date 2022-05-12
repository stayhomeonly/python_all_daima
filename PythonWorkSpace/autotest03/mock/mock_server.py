"""
-------------------------------------------------
   File Name:publish_services01
   Author:Mr.Liu

-------------------------------------------------
"""
# 步骤2：引包
import flask, json, random

# 步骤3： 创建 app对象，把当前模块做为一个服务
app = flask.Flask(__name__)


# 步骤4： 定义接口
@app.route('/getmecode', methods=['post', 'get'])
# 短信登录
def getmecode():
    data = flask.request.values  # 获取用户传入的内容
    phone_number = data.get('phone_number')  # 获取用户转入的username的value值
    if phone_number == '15821598071':
        return json.dumps({"code": 1001, "msg": "手机号码已停机"}, ensure_ascii=False)
    elif phone_number == '15821598072':
        return json.dumps({"code": 1003, "msg": "手机号码已注销"}, ensure_ascii=False)
    else:
        return json.dumps({"code": 1002, "msg": random.randint(1000,9999)}, ensure_ascii=False)


# 步骤5：启动服务
app.run(port=5678, debug=True)  # 发布服务器
