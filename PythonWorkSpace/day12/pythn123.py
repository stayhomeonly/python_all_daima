"""
=========================
File Name:pythn123
Author:pengyumei
Date:2021/12/2-19:02
==========================
"""

import flask, json
from day11.db_utils03 import DBUtils

"""
flask框架介绍: 该框架为后端服务框架,能够部署服务,这样我们的接口/代码就能够使用http协议来调用
"""

app = flask.Flask(__name__)


@app.route('/register', methods=['get', 'post'])
def register():
    data = flask.request.values
    uname = data.get('username')
    pwd = data.get('password')
    re_pwd = data.get('re_password')
    email = data.get('email')
    phone = data.get('phone')

    if len(uname) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(pwd) == 0:
        return json.dumps({"code": 1003, "msg": "密码不能为空"}, ensure_ascii=False)
    elif pwd != re_pwd:
        return json.dumps({"code": 1004, "msg": "两次输入密码不一致"}, ensure_ascii=False)
    elif not (6 <= len(uname) <= 18 and 6 <= len(pwd) <= 18):
        return json.dumps({"code": 1005, "msg": "用户名和密码必须在6-18位之间"}, ensure_ascii=False)
    elif len(email) == 0:
        return json.dumps({"code": 1006, "msg": "邮箱不能为空"}, ensure_ascii=False)
    elif len(phone) == 0:
        return json.dumps({"code": 1007, "msg": "手机号不能为空"}, ensure_ascii=False)
    db = DBUtils()
    count = db.find_count("select * from tb_user where name = %s;", (uname,))
    count1 = db.find_count("select * from tb_user where phone = %s;", (phone,))
    if count1 != 0 and count == 0:
        db.close()
        return json.dumps({"code": 1008, "msg": "手机号已被注册"}, ensure_ascii=False)
    if count != 0:
        db.close()
        return json.dumps({"code": 1009, "msg": "用户名已被注册"}, ensure_ascii=False)
    else:
        ct = db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);", (uname, pwd, email, phone))
        db.close()
        if ct == 1:
            return json.dumps({"code": 9999, "msg": "注册成功!"}, ensure_ascii=False)
        else:
            return json.dumps({"code": 0000, "msg": "注册失败,环境异常,请联系管理员!"}, ensure_ascii=False)


@app.route('/user_login', methods=["get", 'post'])
def user_login():
    data = flask.request.values  # 接收请求发过来的数据
    username = data.get("username")  # 获取请求中的username对应的值
    password = data.get("password")  # 获取请求中的password对应的值
    if len(username) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(password) == 0:
        return json.dumps({"code": 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    else:  # 查询数据库,看看当前传入的用户名和密码在数据库是否存在
        db = DBUtils()
        # 从数据库里查询用户名等于 接口传入的用户名 并且密码 等于从接口传入的密码
        count = db.find_count("select * from tb_user where name = %s and passwd = %s;", (username, password))
        db.close()
        if count == 0 or count == -1:
            return json.dumps({"code": 1003, "msg": "用户名或密码错误"}, ensure_ascii=False)
        else:
            return json.dumps({"code": 9999, "msg": "登录成功"}, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
