"""
=========================
File Name:python_senior13
Author:pengyumei
Date:2021/12/2-15:40
==========================
"""
import flask, json
from autotest01.comms.db_utils import DBUtils

# 第一步：通过 pip install flask 导入该库


# 第二步：创建app对象，把当前的python文件当成一个服务，__name__代表当前的python文件
app = flask.Flask(__name__)  # __name__ 把当前模块导入到app中


# 第三步：将我们的接口发布成服务,route是路由的意思


@app.route('/register', methods=["get", "post"])
def register():
    data = flask.request.values
    uname = data.get("username")

    pwd = data.get('password')
    re_pwd = data.get('re_password')
    phone = data.get('phone')
    email = data.get('email')

    if len(uname) == 0:
        return json.dumps({'code': 1001, 'msg': '登录名不能为空'}, ensure_ascii=False)
    elif len(pwd) == 0:
        return json.dumps({'code': 1002, 'msg': '密码不能为空'}, ensure_ascii=False)
    elif len(pwd) == 0:
        return json.dumps({'code': 1003, 'mag': '确认密码不能为空'}, ensure_ascii=False)
    elif not (6 <= len(uname) < 18 and 6 <= len(pwd) <= 18):
        return json.dumps({'code': 1004, 'msg': '用户名和密码位数不正确'}, ensure_ascii=False)
    elif pwd != re_pwd:
        return json.dumps({'code': 1005, 'msg': '两次密码输入不一致'}, ensure_ascii=False)

    elif len(phone) == 0:
        return json.dumps({'code': 1007, "msg": '手机号码不能为空'}, ensure_ascii=False)
    elif len(email) == 0:
        return json.dumps({'code': 1008, "msg": '邮箱不能为空'}, ensure_ascii=False)

    db = DBUtils()
    count = db.find_count("select * from tb_user where name=%s;", (uname,))
    count1 = db.find_count("select * from tb_user where phone=%s;", (phone,))

    if count1 != 0 and count == 0:
        db.close()
        return json.dumps({"code": 1009, "msg": "手机号码已经被注册"}, ensure_ascii=False)
    if count != 0:
        db.close()
        return json.dumps({"code": 1010, "msg": "用户名已经被注册"}, ensure_ascii=False)
    else:
        ct = db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                    (uname, pwd, email, phone))
        db.close()
        if ct == 1:
            return json.dumps({'code': 9999, "msg": "注册成功"}, ensure_ascii=False)
        else:
            return json.dumps({'code': 0000, "msg": "注册失败，环境异常，请联系管理员"}, ensure_ascii=False)


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
            return json.dumps({"code": 1003, "msg": "用户名或者密码错误"}, ensure_ascii=False)
        else:
            return json.dumps({"code": 9999, "msg": "登录成功"}, ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True)  # 启动服务（使用debug模式启动服务，debug是可调式模式）
