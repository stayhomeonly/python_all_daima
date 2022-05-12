"""
=========================
File Name:python_senior12
Author:pengyumei
Date:2021/12/2-14:43
==========================
"""
'''
flask 框架介绍 ：该框架为后端服务框架，能够部署服务，这样我们的接口/代码就能使用使用http协议来调用
'''

# 第一步：通过 pip install flask 导入该库

import flask, json

# 第二步：创建app对象，把当前的python文件当成一个服务，__name__代表当前的python文件
app = flask.Flask(__name__)  # __name__ 把当前模块导入到app中


# 第三步：将我们的接口发布成服务,route是路由的意思
@app.route('/index', methods=["get", "post"])  # index 在这里是主页的意思,虚拟路径的意思
def index():
    return "tester23班第一个接口服务！"


@app.route('/login', methods=["get", "post"])
def login():
    data = flask.request.values  # 接手请求发过来的数据
    print(
        data)  # CombinedMultiDict([ImmutableMultiDict([('username', 'xiaohua'), ('psaaword', 'a123456')]), ImmutableMultiDict([])])
    username = data.get("username")  # 获取请求中的username对应的值
    password = data.get("password")  # 获取请求中的password对应的值

    if len(username) == 0:
        return json.dumps({'code': 2001, 'msg': '登录名不能为空'}, ensure_ascii=False)  # json.dumps是强转为json格式
    elif len(password) == 0:
        return json.dumps({'code': 2002, 'msg': '密码不能为空'}, ensure_ascii=False)
    elif username == 'xiaohua' and password == 'a123456':
        return json.dumps({'code': 9999, "msg": "登录成功"}, ensure_ascii=False)
    else:
        return json.dumps({"code": 1003, "msg": "用户名或密码错误"}, ensure_ascii=False)


if __name__ == "__main__":
    app.run(port=8888, debug=True)  # 启动服务（使用debug模式启动服务，debug是可调式模式）
