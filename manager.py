# -*- coding:utf-8 -*-
# 程序入口
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
# from iHome import app, db
from iHome import get_app, db

# 使用工厂设计模式创建app
# -----工厂设计模式的成品-----
app = get_app('dev')

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
