# -*- coding:utf-8 -*-
# 程序入口
import redis
from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    """配置参数"""

    DEBUG = True

    # 配置mysql数据库：真实开发应该写数据库的真实ip地址
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/db_iHome_01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库：实际开发也必须填写真实的redis数据库ip
    # 模仿mysql数据库，实际上redis的配置参数，不是从Config中默认读取的
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app = Flask(__name__)

# 加载配置参数
app.config.from_object(Config)


# 创建链接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 创建脚本管理器对象
manager = Manager(app)


@app.route('/')
def index():
    return 'index!'


if __name__ == '__main__':
    manager.run()
