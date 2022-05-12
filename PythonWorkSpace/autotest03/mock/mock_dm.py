"""
-------------------------------------------------
   File Name:publish_services01
   Author:Mr.Liu

-------------------------------------------------
"""
# 步骤2：引包
import flask, json, re, requests
from autotest03.comms.db_utils import DBUtils

# 步骤3： 创建 app对象，把当前模块做为一个服务
app = flask.Flask(__name__)


# 步骤4： 定义接口
@app.route('/massage_login', methods=['post', 'get'])
# 短信登录
def update_password():
    data = flask.request.values  # 获取用户传入的内容
    phone_number = data.get('phone_number')  # 获取用户转入的username的value值
    vfUserCode = data.get('vfUserCode')

    if len(phone_number) == 0:
        return json.dumps({"code": 1001, "msg": "手机号码不能为空"}, ensure_ascii=False)
    elif len(vfUserCode) == 0:
        return json.dumps({"code": 1002, "msg": "短信验证码不能为空"}, ensure_ascii=False)
    else:
        # 模拟从缓存数据库中取数据。
        db = DBUtils()
        vfServerCode = db.find_one('select v_code from m_code where username=%s', (phone_number,))[0]
        db.close()
        if vfUserCode == vfServerCode:
            return json.dumps({"code": 1001, "msg": "登录成功"}, ensure_ascii=False)


# 该接口有三个测试点：
#     1、输入正确的手机号返回验证码
#     2、输入错误格式，返回提示
#     3、输入不存在，非正常状态的手机号，返回错误提示
# 生成验证码：通过手机号，调用第三方接口得到手机号，保存在缓存数据库中。
@app.route('/genMessageCode', methods=['post', 'get'])
def genMessageCode():
    data = flask.request.values  # 获取用户传入的内容
    phone_number = data.get('phone_number')  # 获取用户转入的username的value值
    print(phone_number)
    if not re.match(r'^1\d{10}$', phone_number):
        return json.dumps({"code": 1001, "msg": "phone_number格式错误！"}, ensure_ascii=False)
    else:
        # 调用第三方接口，获取短信验证码
        response = requests.post(
            url="http://127.0.0.1:5678/getmecode",
            data={'phone_number': phone_number}
        )
        result = response.json()
        print(result)
        print(result.get('msg'))
        # 将短信验证码保存在缓存数据库中，这里我们使用 mysql模拟
        if isinstance(result.get('msg'), int):
            db = DBUtils()
            db.cud('insert into m_code values(%s,%s)', (phone_number, result.get('msg')))
            db.close()
            return json.dumps({"code": 1002, "msg": '验证码为:' + str(result.get('msg'))}, ensure_ascii=False)
        return json.dumps({"code": 1002, "msg": '手机号码无效'}, ensure_ascii=False)


# 步骤5：启动服务
app.run(port=6767, debug=True)  # 发布服务器
