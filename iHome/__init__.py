# -*- coding:utf-8 -*-
# 创建应用实例

import redis
from flask import Flask,session
from flask_session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from config import Config, Development, Production, UnitTest

app = Flask(__name__)

# 加载配置参数
app.config.from_object(Development)

# 创建链接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Development.REDIS_HOST, port=Development.REDIS_PORT)

# 开启CSRF保护:flask需要自己讲csrf_token写入到浏览器的cookie
CSRFProtect(app)

# 使用flask_session将session数据写入到redis数据库
Session(app)