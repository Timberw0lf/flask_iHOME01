# -*- coding:utf-8 -*-
# 程序入口
import redis
from flask import Flask,session
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask_session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect


class Config(object):
    """配置参数"""

    DEBUG = True

    # 秘钥
    SECRET_KEY = 'q7pBNcWPgmF6BqB6b5VICF7z7pI+90o0O4CaJsFGjzRsYiya9SEgUDytXvzFsIaR'

    # 配置mysql数据库：真实开发应该写数据库的真实ip地址
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/db_iHome_01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库：实际开发也必须填写真实的redis数据库ip
    # 模仿mysql数据库，实际上redis的配置参数，不是从Config中默认读取的
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置session参数
    # 指定session存储到redis
    SESSION_TYPE = 'redis'
    # 指定要使用的redis的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 是否使用secret_key签名session_data
    SESSION_USE_SIGNER = True
    # 设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 3600 * 24  # 有效期为一天


app = Flask(__name__)

# 加载配置参数
app.config.from_object(Config)


# 创建链接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF保护:flask需要自己讲csrf_token写入到浏览器的cookie
CSRFProtect(app)

# 使用flask_session将session数据写入到redis数据库
Session(app)

# 创建脚本管理器对象
manager = Manager(app)

# 让迁移时，app和db建立关联，app在前，db在后（ctrl+p）
Migrate(app, db)

# 将数据库迁移的脚本、命令添加到脚本管理器对象
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return 'index!'


if __name__ == '__main__':
    # 记得在edit_configurations 的script parameters中填写 runserver
    manager.run()
