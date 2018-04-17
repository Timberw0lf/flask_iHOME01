# -*- coding:utf-8 -*-
# 创建应用实例

import redis
from flask import Flask,session
from flask_session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
# from config import Config, Development, Production, UnitTest
from config import configs

# 但是，用工厂设计模式创建app，将db也写进了方法之中，导致manager文件无法获取db,
# 即无法使迁移数据时，app和db建立关联，故将db = SQLAlchemy(app)写到方法外面来，
# 创建一个SQLAlchemy()的实例对象,但是问题又来了，app也被写进了方法里面，外面也调不到，
# 查看SQLAlchemy源代码，发现db = SQLAlchemy(app)的本质即：
# if app is not None时执行self.init_app(app)，那么我们可以分两步走：
# 1> db = SQLAlchemy()
# 2> db = init_app(app)

# 第一步：在方法外面创建SQLAlchemy实例：db;方便manager调用
db = SQLAlchemy()

# 使用工厂设计模式，将创建app的代码，改写为一个生成app(flask实例)的方法，
# 通过给方法传参数，让业务逻辑模块可以根据传入的参数（原料），选择不同的配置，创建app
# -----工厂设计模式的工厂-----
def get_app(config_name):

    app = Flask(__name__)

    # 加载配置参数
    app.config.from_object(configs[config_name])

    # 创建链接到mysql数据库的对象
    # db = SQLAlchemy(app)
    # 第二步：建立app与mysql的连接
    db.init_app(app)

    # 创建连接到redis数据库的对象
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)

    # 开启CSRF保护:flask需要自己讲csrf_token写入到浏览器的cookie
    CSRFProtect(app)

    # 使用flask_session将session数据写入到redis数据库
    Session(app)

    return app

