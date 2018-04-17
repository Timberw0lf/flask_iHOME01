# -*- coding:utf-8 -*-
# 创建应用实例

import redis
from flask import Flask,session
from flask_session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
# from config import Config, Development, Production, UnitTest
from config import configs


# 使用工厂设计模式，将创建app的代码，改写为一个生成app的方法，
# 通过给方法传参数，让业务逻辑模块可以根据传入的参数（原料），选择不同的配置，创建app
# -----工厂设计模式的工厂-----
def get_app(config_name):

    app = Flask(__name__)

    # 加载配置参数
    app.config.from_object(configs[config_name])

    # 创建链接到mysql数据库的对象
    db = SQLAlchemy(app)

    # 创建连接到redis数据库的对象
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)

    # 开启CSRF保护:flask需要自己讲csrf_token写入到浏览器的cookie
    CSRFProtect(app)

    # 使用flask_session将session数据写入到redis数据库
    Session(app)

    return app