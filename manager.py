# -*- coding:utf-8 -*-
# 程序入口
import redis
from flask import Flask,session
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask_session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from config import Config


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
